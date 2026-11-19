#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Comprehensive System for Customer, Service, and Reservation Management - Software FJ
Programming Course - Code: 213023 - UNAD
Original Developers: Andrés Ovidio Tobar Ladino and Livan Jussete Vargas Perdomo
Description: Object-oriented application with abstract classes,
inheritance, polymorphism, encapsulation, and advanced exception handling.
"""

# Import ABC and abstractmethod to create abstract classes and methods.
from abc import ABC, abstractmethod

# Import logging to save events and errors to a file.
import logging

# Import datetime to record the execution date and time.
import datetime

# Import math to verify that numeric values are finite.
import math


# =====================================================================
# LOGGING SYSTEM CONFIGURATION (ERROR AND EVENT AUDIT)
# =====================================================================

# Configure the file where events and errors will be saved.
logging.basicConfig(
    filename="system_management.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    encoding="utf-8"
)


# =====================================================================
# CUSTOM EXCEPTIONS AND CHAINING
# =====================================================================

# General application exception.
class SoftwareFJError(Exception):
    """Base class for custom exceptions in the Software FJ system."""
    pass


# Exception for incorrect personal data.
class InvalidCustomerError(SoftwareFJError):
    """Raised when customer data does not pass validations."""
    pass


# Exception for unavailable services or parameters.
class ServiceNotAvailableError(SoftwareFJError):
    """Raised when a service or its parameters are incorrect."""
    pass


# Exception for errors during reservation processing.
class ReservationError(SoftwareFJError):
    """Raised upon failures in reservation creation or processing."""
    pass


# =====================================================================
# AUXILIARY VALIDATION FUNCTIONS
# =====================================================================

def validate_text(value, field, min_length=1):
    """Verifies that data is text and has the required minimum length."""
    if not isinstance(value, str) or len(value.strip()) < min_length:
        raise ValueError(f"The field {field} must contain at least "
                         f"{min_length} character(s).")
    return value.strip()


def validate_positive_number(value, field, allow_zero=False):
    """Verifies that a value is numeric, finite, and positive."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"The field {field} must be a number.")

    if not math.isfinite(value):
        raise ValueError(f"The field {field} must be a finite number.")

    if allow_zero:
        if value < 0:
            raise ValueError(f"The field {field} cannot be negative.")
    elif value <= 0:
        raise ValueError(f"The field {field} must be greater than zero.")

    return value


# =====================================================================
# ABSTRACT BASE CLASS (GENERAL ENTITY)
# =====================================================================

class BaseEntity(ABC):
    """Abstract class representing general system entities."""

    def __init__(self, identifier: str):
        # Validates and stores the entity identifier.
        try:
            self._identifier = validate_text(
                identifier, "identifier", 3
            )
        except ValueError as error:
            logging.error("Invalid identifier: %s", error)
            raise SoftwareFJError("It was not possible to create the entity.") from error

    @property
    def identifier(self) -> str:
        """Allows querying the identifier without modifying it directly."""
        return self._identifier

    @abstractmethod
    def detail_entity(self) -> str:
        """Forces derived classes to implement the entity detail."""
        pass


# =====================================================================
# CUSTOMER CLASS WITH ENCAPSULATION AND STRICT VALIDATIONS
# =====================================================================

class Customer(BaseEntity):
    """Represents a registered customer in the Software FJ company."""

    def __init__(self, identifier: str, name: str, national_id: str,
                 email: str, phone: str):
        # Initializes the identifier inherited from BaseEntity.
        super().__init__(identifier)

        # Assigns data through properties to apply validations.
        self.name = name
        self.national_id = national_id
        self.email = email
        self.phone = phone

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        # Verifies that the name is text and has at least three characters.
        try:
            self._name = validate_text(value, "name", 3)
        except ValueError as error:
            logging.error("Invalid customer name: %s", error)
            raise InvalidCustomerError(str(error)) from error

    @property
    def national_id(self) -> str:
        return self._national_id

    @national_id.setter
    def national_id(self, value: str):
        # The national ID is handled as text to preserve all its digits.
        if not isinstance(value, str) or not value.isdigit() or len(value) < 7:
            message = "The national ID must contain at least 7 numeric digits."
            logging.error("Invalid national ID: %r", value)
            raise InvalidCustomerError(message)
        self._national_id = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        # Checks for a basic email structure.
        if not isinstance(value, str):
            logging.error("Email must be text.")
            raise InvalidCustomerError("The email address must be text.")

        clean_email = value.strip()
        parts = clean_email.split("@")

        if (len(parts) != 2 or not parts[0] or
                "." not in parts[1] or parts[1].startswith(".") or
                parts[1].endswith(".")):
            logging.error("Invalid email address: %r", value)
            raise InvalidCustomerError("The email address is not valid.")

        self._email = clean_email

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        # Checks that the phone contains at least seven digits.
        if not isinstance(value, str) or not value.isdigit() or len(value) < 7:
            logging.error("Invalid phone number: %r", value)
            raise InvalidCustomerError(
                "The phone number must contain at least 7 numeric digits."
            )
        self._phone = value

    def detail_entity(self) -> str:
        """Returns the main customer data."""
        return (
            f"Customer [ID: {self._identifier}, Name: {self._name}, "
            f"ID Number: {self._national_id}, Email: {self._email}]"
        )


# =====================================================================
# ABSTRACT SERVICE CLASS AND SPECIALIZED SERVICES (POLYMORPHISM)
# =====================================================================

class Service(BaseEntity, ABC):
    """Abstract class defining the structure of Software FJ services."""

    def __init__(self, identifier: str, service_name: str,
                 base_cost: float):
        # Initializes the identifier and validates the name and cost.
        super().__init__(identifier)

        try:
            self.service_name = validate_text(
                service_name, "service name", 3
            )
        except ValueError as error:
            logging.error("Invalid service name: %s", error)
            raise ServiceNotAvailableError(str(error)) from error

        self.base_cost = base_cost

    @property
    def base_cost(self) -> float:
        return self._base_cost

    @base_cost.setter
    def base_cost(self, value: float):
        # Prevents negative costs, non-numeric values, and infinite values.
        try:
            validate_positive_number(value, "base cost", allow_zero=True)
            self._base_cost = float(value)
        except ValueError as error:
            logging.error("Invalid base cost: %s", error)
            raise ServiceNotAvailableError(str(error)) from error

    @abstractmethod
    def calculate_cost(self, *args, **kwargs) -> float:
        """Polymorphic method that each service implements in a particular way."""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Forces description of each service type."""
        pass

    @abstractmethod
    def validate_parameters(self):
        """Forces validation of particular parameters for each service."""
        pass

    def detail_entity(self) -> str:
        """Returns the name and base cost of the service."""
        return (
            f"Service: {self.service_name} "
            f"(Base: ${self._base_cost:,.2f})"
        )


# =====================================================================
# 1. SPECIALIZED SERVICE: ROOM RESERVATION
# =====================================================================

class RoomReservation(Service):
    """Manages executive and conference room reservations."""

    def __init__(self, identifier: str, service_name: str,
                 base_cost: float, person_capacity: int):
        # Initializes common service attributes.
        super().__init__(identifier, service_name, base_cost)

        # Stores capacity and validates particular parameters.
        self.person_capacity = person_capacity
        self.validate_parameters()

    def validate_parameters(self):
        """Verifies that room capacity is an integer greater than zero."""
        if (isinstance(self.person_capacity, bool) or
                not isinstance(self.person_capacity, int) or
                self.person_capacity <= 0):
            message = "Room capacity must be an integer greater than zero."
            logging.error(message)
            raise ServiceNotAvailableError(message)

    def calculate_cost(self, hours: int, discount_percentage: float = 0.0,
                       apply_tax: bool = True) -> float:
        """
        Calculates room cost.
        Optional parameters allow applying discounts and taxes.
        """
        try:
            validate_positive_number(hours, "reservation hours")
            validate_positive_number(
                discount_percentage, "discount", allow_zero=True
            )

            if discount_percentage > 100:
                raise ValueError("Discount cannot exceed 100%.")

            if not isinstance(apply_tax, bool):
                raise ValueError("Tax option must be True or False.")

            # Calculates subtotal according to reserved hours.
            subtotal = self.base_cost * hours

            # Applies requested discount.
            discount = subtotal * (discount_percentage / 100)
            discounted_amount = subtotal - discount

            # Applies 19% tax when applicable.
            tax = discounted_amount * 0.19 if apply_tax else 0.0

            # Returns total rounded to two decimals.
            return round(discounted_amount + tax, 2)

        except (ValueError, TypeError) as error:
            logging.error("Error calculating cost in RoomReservation: %s", error)
            raise ReservationError(
                "Failure in room financial calculation."
            ) from error

    def get_description(self) -> str:
        """Returns the description of the room and its capacity."""
        return (
            f"Room Reservation '{self.service_name}' "
            f"(Capacity: {self.person_capacity} people)."
        )


# =====================================================================
# 2. SPECIALIZED SERVICE: EQUIPMENT RENTAL
# =====================================================================

class EquipmentRental(Service):
    """Manages the rental of specialized equipment and servers."""

    def __init__(self, identifier: str, service_name: str,
                 base_cost: float, equipment_serial: str):
        # Initializes common service attributes.
        super().__init__(identifier, service_name, base_cost)

        # Stores serial and verifies it is valid.
        self.equipment_serial = equipment_serial
        self.validate_parameters()

    def validate_parameters(self):
        """Verifies that the equipment serial has at least three characters."""
        try:
            self.equipment_serial = validate_text(
                self.equipment_serial, "equipment serial", 3
            )
        except ValueError as error:
            logging.error("Invalid equipment serial: %s", error)
            raise ServiceNotAvailableError(str(error)) from error

    def calculate_cost(self, days: int, additional_insurance: float = 0.0) -> float:
        """Calculates rental based on days and optional additional insurance."""
        try:
            validate_positive_number(days, "rental days")
            validate_positive_number(
                additional_insurance, "additional insurance", allow_zero=True
            )

            # Sums daily cost multiplied by days plus insurance.
            total = (self.base_cost * days) + additional_insurance
            return round(total, 2)

        except (ValueError, TypeError) as error:
            logging.error("Error calculating cost in EquipmentRental: %s", error)
            raise ReservationError(
                "Failure in equipment rental calculation."
            ) from error

    def get_description(self) -> str:
        """Returns the description of the rented equipment."""
        return (
            f"Equipment Rental '{self.service_name}' "
            f"- Serial: {self.equipment_serial}."
        )


# =====================================================================
# 3. SPECIALIZED SERVICE: SPECIALIZED CONSULTING
# =====================================================================

class SpecializedConsulting(Service):
    """Manages professional consulting and advisory services in software engineering."""

    def __init__(self, identifier: str, service_name: str,
                 base_cost: float, specialty: str):
        # Initializes common service attributes.
        super().__init__(identifier, service_name, base_cost)

        # Stores specialty and verifies its content.
        self.specialty = specialty
        self.validate_parameters()

    def validate_parameters(self):
        """Verifies that the specialty is not empty."""
        try:
            self.specialty = validate_text(
                self.specialty, "specialty", 3
            )
        except ValueError as error:
            logging.error("Invalid specialty: %s", error)
            raise ServiceNotAvailableError(str(error)) from error

    def calculate_cost(self, sessions: int,
                       high_complexity: bool = False) -> float:
        """Calculates cost by sessions and considers optional complexity."""
        try:
            validate_positive_number(sessions, "sessions")

            if not isinstance(high_complexity, bool):
                raise ValueError(
                    "High complexity must be indicated with True or False."
                )

            # If complexity is high, a 25% multiplier is applied.
            multiplier = 1.25 if high_complexity else 1.0

            # Calculates and returns total cost.
            total = self.base_cost * sessions * multiplier
            return round(total, 2)

        except (ValueError, TypeError) as error:
            logging.error(
                "Error calculating cost in SpecializedConsulting: %s", error
            )
            raise ReservationError(
                "Failure in consulting calculation."
            ) from error

    def get_description(self) -> str:
        """Returns the description of the consulting and its specialty."""
        return (
            f"Specialized Consulting in '{self.specialty}' "
            f"- Service: {self.service_name}."
        )


# =====================================================================
# RESERVATION CLASS (INTEGRATION AND ROBUST EXCEPTION HANDLING)
# =====================================================================

class Reservation:
    """Relates a customer, a service, its duration, and the reservation status."""

    reservation_counter = 2000

    def __init__(self, customer: Customer, service: Service,
                 duration_parameter: int, cost_kwargs: dict):
        # Verifies that objects of the corresponding classes are received.
        if not isinstance(customer, Customer):
            raise ReservationError("The reservation requires a valid customer.")

        if not isinstance(service, Service):
            raise ReservationError("The reservation requires a valid service.")

        # Verifies that duration is a positive number.
        try:
            validate_positive_number(duration_parameter, "duration")
        except ValueError as error:
            logging.error("Invalid duration when creating reservation: %s", error)
            raise ReservationError("The reservation duration is not valid.") from error

        # Verifies that additional parameters are organized in a dictionary.
        if not isinstance(cost_kwargs, dict):
            raise ReservationError("Cost parameters must be in a dictionary.")

        # Assigns a unique identifier to the reservation.
        self.id_reserva = f"RES-{Reservation.reservation_counter}"
        Reservation.reservation_counter += 1

        # Stores objects and parameters related to the reservation.
        self.customer = customer
        self.service = service
        self.duration_parameter = duration_parameter
        self.cost_kwargs = cost_kwargs.copy()

        # Establishes initial status and pending cost.
        self.status = "Pending"
        self.total_cost = 0.0

        # Logs the creation of the reservation.
        logging.info("Reservation %s was created.", self.id_reserva)

    def process_reservation(self):
        """Processes the reservation using try, except, else, and finally."""
        print(f"\n--- Processing Reservation: {self.id_reserva} ---")
        logging.info("Starting processing of reservation %s.", self.id_reserva)

        try:
            # Prevents reprocessing a reservation that has already been closed.
            if self.status != "Pending":
                raise ReservationError(
                    f"Cannot process a reservation in status {self.status}."
                )

            # Re-verifies objects before calculation.
            if not isinstance(self.customer, Customer):
                raise ReservationError("Invalid customer instance.")

            if not isinstance(self.service, Service):
                raise ReservationError("Invalid service instance.")

            # Performs polymorphic calculation according to service type.
            self.total_cost = self.service.calculate_cost(
                self.duration_parameter, **self.cost_kwargs
            )

            # Confirms the reservation when calculation completes successfully.
            self.status = "Confirmed"

        except (InvalidCustomerError, ServiceNotAvailableError, ReservationError) as error:
            # Logs controlled validation or reservation errors.
            self.status = "Failed"
            logging.warning(
                "Operational warning in %s: %s", self.id_reserva, error
            )
            print(f"[WARNING] Reservation not completed: {error}")
            raise

        except Exception as error:
            # Captures unexpected errors and preserves original cause.
            self.status = "Critical Error"
            logging.exception(
                "Severe error processing reservation %s.", self.id_reserva
            )
            print(f"[CRITICAL ERROR] Unexpected exception: {error}")
            raise ReservationError(
                f"Severe failure processing reservation {self.id_reserva}."
            ) from error

        else:
            # This block runs only when there were no exceptions.
            logging.info(
                "Reservation %s processed. Total: $%.2f",
                self.id_reserva, self.total_cost
            )
            print(
                f"[SUCCESS] Reservation {self.id_reserva} confirmed "
                f"for customer {self.customer.name}."
            )
            print(f"        Detail: {self.service.get_description()}")
            print(f"        Total Cost: ${self.total_cost:,.2f}")

        finally:
            # This block always runs, whether an error occurred or not.
            print(
                f"[FINAL STATUS] Operation for {self.id_reserva} "
                f"concluded with status: {self.status}."
            )
            logging.info(
                "Closing cycle for reservation %s. Status: %s.",
                self.id_reserva, self.status
            )

    def cancel_reservation(self):
        """Cancels a reservation that has not yet been cancelled."""
        try:
            if self.status == "Cancelled":
                raise ReservationError("The reservation is already cancelled.")

            if self.status == "Critical Error":
                raise ReservationError(
                    "Cannot cancel a reservation with a critical error."
                )

            # Updates status and logs cancellation.
            self.status = "Cancelled"
            logging.info(
                "Reservation %s was cancelled by the user.", self.id_reserva
            )
            print(
                f"[CANCELLATION] Reservation {self.id_reserva} "
                "was successfully cancelled."
            )

        except ReservationError as error:
            logging.error("It was not possible to cancel the reservation: %s", error)
            print(f"[CANCELLATION ERROR] {error}")
            raise


# =====================================================================
# SIMULATION OF MORE THAN 10 COMPLETE OPERATIONS (UNAD REQUIREMENT)
# =====================================================================

def execute_system_simulation():
    """Executes valid and invalid operations to test the system."""

    # Displays execution header and current date.
    print("=================================================================")
    print("      SYSTEM SIMULATION - SOFTWARE FJ (PHASE 4)                 ")
    print("      Developed by: Andrés Ovidio Tobar Ladino and Livan Jussete Vargas Perdomo")
    print("      Date and time:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("=================================================================\n")

    # Creates internal lists to manage objects in memory.
    customer_list = []
    service_list = []
    reservation_list = []

    # ---------------------------------------------------------------
    # OPERATION 1: VALID CUSTOMER REGISTRATION 1
    # ---------------------------------------------------------------
    print("\n--- Operation 1: Valid Customer Registration ---")
    try:
        c1 = Customer(
            "CLI-01", "Andrés Tobar", "1012345678",
            "andres.tobar@unad.edu.co", "3101234567"
        )
        customer_list.append(c1)
    except (InvalidCustomerError, SoftwareFJError) as error:
        logging.error("Operation 1 failed: %s", error)
        print(f"Error: {error}")
    else:
        print(f"Success: {c1.detail_entity()}")
    finally:
        logging.info("Operation 1 finished.")

    # ---------------------------------------------------------------
    # OPERATION 2: INVALID CUSTOMER REGISTRATION
    # ---------------------------------------------------------------
    print("\n--- Operation 2: Invalid Customer Registration ---")
    try:
        c_err = Customer(
            "CLI-02", "María Pérez", "ABC12345",
            "maria@gmail.com", "3209876543"
        )
        customer_list.append(c_err)
    except InvalidCustomerError as error:
        logging.warning("Operation 2: customer rejected: %s", error)
        print(f"Exception successfully controlled: {error}")
    finally:
        logging.info("Operation 2 finished.")

    # ---------------------------------------------------------------
    # OPERATION 3: VALID CUSTOMER REGISTRATION 2
    # ---------------------------------------------------------------
    print("\n--- Operation 3: Valid Customer Registration 2 ---")
    try:
        c2 = Customer(
            "CLI-03", "Carlos Gómez", "1098765432",
            "carlos.gomez@gmail.com", "3159876543"
        )
        customer_list.append(c2)
    except (InvalidCustomerError, SoftwareFJError) as error:
        logging.error("Operation 3 failed: %s", error)
        print(f"Error: {error}")
    else:
        print(f"Success: {c2.detail_entity()}")
    finally:
        logging.info("Operation 3 finished.")

    # ---------------------------------------------------------------
    # OPERATION 4: CORRECT SERVICE CREATION (ROOM)
    # ---------------------------------------------------------------
    print("\n--- Operation 4: Correct Service Creation (Room) ---")
    try:
        s1 = RoomReservation(
            "SRV-01", "Main Boardroom", 60000.0, 20
        )
        service_list.append(s1)
    except (ServiceNotAvailableError, SoftwareFJError) as error:
        logging.error("Operation 4 failed: %s", error)
        print(f"Error: {error}")
    else:
        print(f"Success: {s1.detail_entity()}")
    finally:
        logging.info("Operation 4 finished.")

    # ---------------------------------------------------------------
    # OPERATION 5: INCORRECT SERVICE CREATION
    # ---------------------------------------------------------------
    print("\n--- Operation 5: Incorrect Service Creation ---")
    try:
        s_err = RoomReservation(
            "SRV-02", "Beta Room", -5000.0, 10
        )
        service_list.append(s_err)
    except ServiceNotAvailableError as error:
        logging.warning("Operation 5: service rejected: %s", error)
        print(f"Exception successfully controlled: {error}")
    finally:
        logging.info("Operation 5 finished.")

    # ---------------------------------------------------------------
    # OPERATION 6: CORRECT SERVICE CREATION (RENTAL)
    # ---------------------------------------------------------------
    print("\n--- Operation 6: Correct Service Creation (Equipment Rental) ---")
    try:
        s2 = EquipmentRental(
            "SRV-03", "High-Performance Server",
            150000.0, "SRV-DELL-9922"
        )
        service_list.append(s2)
    except (ServiceNotAvailableError, SoftwareFJError) as error:
        logging.error("Operation 6 failed: %s", error)
        print(f"Error: {error}")
    else:
        print(f"Success: {s2.detail_entity()}")
    finally:
        logging.info("Operation 6 finished.")

    # ---------------------------------------------------------------
    # OPERATION 7: CORRECT SERVICE CREATION (CONSULTING)
    # ---------------------------------------------------------------
    print("\n--- Operation 7: Correct Service Creation (Consulting) ---")
    try:
        s3 = SpecializedConsulting(
            "SRV-04", "Software Architecture Consulting",
            100000.0, "Software Engineering"
        )
        service_list.append(s3)
    except (ServiceNotAvailableError, SoftwareFJError) as error:
        logging.error("Operation 7 failed: %s", error)
        print(f"Error: {error}")
    else:
        print(f"Success: {s3.detail_entity()}")
    finally:
        logging.info("Operation 7 finished.")

    # ---------------------------------------------------------------
    # OPERATION 8: SUCCESSFUL ROOM RESERVATION WITH DISCOUNT AND TAX
    # ---------------------------------------------------------------
    print("\n--- Operation 8: Successful Reservation (Room) ---")
    try:
        res1 = Reservation(
            customer_list[0], service_list[0],
            duration_parameter=3,
            cost_kwargs={
                "discount_percentage": 15.0,
                "apply_tax": True
            }
        )
        res1.process_reservation()
        reservation_list.append(res1)
    except (ReservationError, IndexError, TypeError) as error:
        logging.error("Operation 8 failed: %s", error)
        print(f"Failure: {error}")
    finally:
        logging.info("Operation 8 finished.")

    # ---------------------------------------------------------------
    # OPERATION 9: SUCCESSFUL RENTAL RESERVATION WITH INSURANCE
    # ---------------------------------------------------------------
    print("\n--- Operation 9: Successful Reservation (Equipment Rental) ---")
    try:
        res2 = Reservation(
            customer_list[1], service_list[1],
            duration_parameter=4,
            cost_kwargs={"additional_insurance": 30000.0}
        )
        res2.process_reservation()
        reservation_list.append(res2)
    except (ReservationError, IndexError, TypeError) as error:
        logging.error("Operation 9 failed: %s", error)
        print(f"Failure: {error}")
    finally:
        logging.info("Operation 9 finished.")

    # ---------------------------------------------------------------
    # OPERATION 10: FAILED RESERVATION DUE TO ZERO DURATION
    # ---------------------------------------------------------------
    print("\n--- Operation 10: Failed Reservation (Zero Duration) ---")
    try:
        res3 = Reservation(
            customer_list[0], service_list[2],
            duration_parameter=0,
            cost_kwargs={"high_complexity": True}
        )
        res3.process_reservation()
        reservation_list.append(res3)
    except (ReservationError, IndexError, TypeError) as error:
        logging.warning("Operation 10: reservation rejected: %s", error)
        print(f"Exception successfully caught: {error}")
    finally:
        logging.info("Operation 10 finished.")

    # ---------------------------------------------------------------
    # OPERATION 11: CANCELLATION OF EXISTING RESERVATION
    # ---------------------------------------------------------------
    print("\n--- Operation 11: Reservation Cancellation ---")
    try:
        if reservation_list:
            reservation_list[0].cancel_reservation()
        else:
            raise ReservationError("No reservations exist to cancel.")
    except ReservationError as error:
        logging.error("Operation 11 failed: %s", error)
        print(f"Could not cancel: {error}")
    finally:
        logging.info("Operation 11 finished.")

    # ---------------------------------------------------------------
    # FINAL SIMULATION SUMMARY
    # ---------------------------------------------------------------
    print("\n=================================================================")
    print("                 SIMULATION SUMMARY                             ")
    print("=================================================================")
    print(f"Total valid customers registered: {len(customer_list)}")
    print(f"Total valid services created: {len(service_list)}")
    print(f"Total reservations managed: {len(reservation_list)}")
    print("Simulation successfully completed. Check 'system_management.log'.")
    print("=================================================================\n")


if __name__ == "__main__":
    execute_system_simulation()