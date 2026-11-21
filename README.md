Sistema Integral de Gestión de Clientes.

**1. DESCRIPCION DEL PROYECTO**

SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES es un proyecto desarrollado en Python para gestionar clientes, servicios y reservas mediante una aplicación basada en programación orientada a objetos.

El propósito principal del sistema es representar un proceso de gestión empresarial en el que se puedan registrar clientes, definir diferentes tipos de servicios, calcular sus respectivos costos y administrar las reservas realizadas.

El desarrollo permite aplicar conceptos fundamentales de programación, como clases, objetos, herencia, encapsulamiento, polimorfismo, clases abstractas y manejo de excepciones. Además, incorpora un sistema de registro de eventos y errores mediante archivos de log, lo que facilita el seguimiento de las operaciones realizadas.

Este proyecto se desarrolla en el contexto del curso de Programación de la Universidad Nacional Abierta y a Distancia (UNAD), como ejercicio práctico de aplicación de los conocimientos adquiridos durante el proceso de formación académica.

**2. OBJETIVO DEL PROYECTO**

Desarrollar un sistema de gestión utilizando el lenguaje de programación Python, aplicando los principios de la programación orientada a objetos para organizar la información de clientes, administrar diferentes tipos de servicios, procesar reservas y controlar posibles errores durante la ejecución.

**3. FUNCIONALIDADES PRINCIPALES**

EL **SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES** incorpora las siguientes funcionalidades:

**3.1. Gestión de clientes**

Permite crear y registrar clientes mediante información básica, como:

Identificador del cliente.

Nombre completo.

Documento de identificación.

Correo electrónico.

Número de teléfono.

También incorpora validaciones para evitar el ingreso de información incorrecta o incompleta.

**3.2. Administración de servicios**

El sistema contempla tres modalidades de servicios:

Reserva de salas: permite gestionar espacios para reuniones y eventos, teniendo en cuenta la capacidad disponible, el tiempo de reserva, los descuentos y los impuestos.

Alquiler de equipos: permite representar el alquiler de equipos especializados y servidores, calculando el costo según los días de utilización y los seguros adicionales.

Consultoría especializada: permite gestionar servicios de asesoría profesional, calculando su valor según el número de sesiones y el nivel de complejidad.

**3.3. Gestión de reservas**

Permite relacionar un cliente con un servicio determinado, establecer su duración y calcular el valor correspondiente.

Las reservas manejan diferentes estados:

Pending: reserva pendiente de procesamiento.

Confirmed: reserva confirmada.

Failed: reserva que no pudo procesarse.

Critical Error: operación que presentó un error inesperado.

Cancelled: reserva cancelada.

**3.4. Cálculo de costos**

Cada modalidad de servicio cuenta con su propio procedimiento de cálculo.

El sistema contempla descuentos, impuestos, seguros adicionales y recargos por complejidad, dependiendo del servicio seleccionado.

**3.5. Validación y manejo de excepciones**

Se implementan mecanismos para identificar y controlar situaciones que puedan afectar el funcionamiento del programa.

Se utilizan excepciones personalizadas para representar errores relacionados con los clientes, los servicios y las reservas.

También se emplean estructuras try, except, else y finally para controlar diferentes situaciones durante la ejecución.

**3.6. Registro de eventos (Logging)**

El programa incorpora un sistema de registro que almacena información sobre las operaciones realizadas y los errores presentados.

Los registros se guardan automáticamente en el archivo:

system_management.log

Este archivo permite consultar los eventos generados durante la ejecución del programa.

**4. CONCEPTOS DE PROGRAMACION APLICADOS**

Durante el desarrollo del proyecto se utilizan los siguientes conceptos:

Concepto

Aplicación en el proyecto

Programación orientada a objetos

Organización del sistema mediante clases y objetos.

Clases y objetos

Representación de clientes, servicios y reservas.

Herencia

Reutilización de características de las clases principales.

Encapsulamiento

Protección y validación de los atributos de los objetos.

Polimorfismo

Implementación de diferentes cálculos según el tipo de servicio.

Clases abstractas

Definición de estructuras generales para clientes y servicios.

Excepciones personalizadas

Control de errores específicos del sistema.

Logging

Registro de eventos, advertencias y errores.

Validaciones

Comprobación de los datos ingresados y parámetros utilizados.

**5. Tecnologías utilizadas**

Para desarrollar y ejecutar el proyecto se utilizan:

Lenguaje de programación: Python.

Biblioteca ABC: implementación de clases y métodos abstractos.

Biblioteca Logging: registro de eventos y errores.

Biblioteca Datetime: manejo de fechas y horas.

Biblioteca Math: validación de valores numéricos.

Las bibliotecas utilizadas pertenecen a la biblioteca estándar de Python, por lo que no se requieren instalaciones adicionales de paquetes externos para ejecutar el programa.

Las bibliotecas utilizadas pertenecen a la biblioteca estándar de Python, por lo que no se requieren instalaciones adicionales de paquetes externos para ejecutar el programa.
