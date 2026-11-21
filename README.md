**SISTEMA INTEGRAL DE GESTION DE CLIENTES.**

**1. DESCRIPCION DEL PROYECTO**

El SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES es un proyecto desarrollado en Python para gestionar clientes, servicios y reservas mediante una aplicación basada en programación orientada a objetos.

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

## 6. Requisitos para ejecutar el proyecto

Para ejecutar correctamente el programa se necesita:

- Tener Python instalado en el equipo.
- Contar con un editor de código, como Visual Studio Code.
- Descargar o copiar el repositorio de GitHub.

## 7. Instrucciones de ejecución

**Paso 1.** Descargar el proyecto desde el repositorio de GitHub.

**Paso 2.** Abrir la carpeta del proyecto en Visual Studio Code.

**Paso 3.** Abrir una terminal y ubicarse en la carpeta donde se encuentra el archivo Python.

**Paso 4.** Ejecutar el siguiente comando:

python sistema.py luego oprimir enter 

Si se conserva el nombre original del archivo, se debe utilizar:

python "sistema.py"

**Paso 5.** Una vez ejecutado, el programa realizará automáticamente una simulación de diferentes operaciones relacionadas con el registro de clientes, creación de servicios, procesamiento y cancelación de reservas.

Al finalizar, se mostrará un resumen de las operaciones realizadas y se generará el archivo `system_management.log` con los registros correspondientes.

## 8. Pruebas y simulación del sistema

El programa incorpora una simulación de 11 operaciones para comprobar el comportamiento de sus funcionalidades.

Durante esta simulación se realizan registros válidos e inválidos de clientes, creación de servicios, validaciones, procesamiento de reservas, cálculos de costos y cancelaciones.

Estas pruebas permiten observar cómo responde el sistema ante diferentes situaciones y cómo se controlan los errores durante su ejecución.

## 9. Estructura general del proyecto

La organización lógica del programa comprende los siguientes componentes:

- Configuración del sistema de registro de eventos.
- Definición de excepciones personalizadas.
- Funciones auxiliares de validación.
- Clase base abstracta para las entidades.
- Clase de gestión de clientes.
- Clase abstracta para los servicios.
- Clases especializadas para cada modalidad de servicio.
- Clase encargada de administrar las reservas.
- Función principal para ejecutar la simulación.

## 10. Alcance del proyecto

Sistema de gestion de clientes representa un ejercicio académico para demostrar la aplicación de los principios de programación orientada a objetos en un escenario de gestión empresarial.

La información de clientes, servicios y reservas se administra en memoria durante la ejecución del programa. No se implementa una conexión con bases de datos ni un sistema de almacenamiento permanente de estos registros.

El archivo de log sí permite conservar un historial de los eventos y errores generados.

## 11. Autores

**Desarrolladores:**

- Andrés Ovidio Tobar Ladino.
- Livan Jussete Vargas Perdomo.

**Institución:** Universidad Nacional Abierta y a Distancia (UNAD).

**Programa académico:** Ingeniería de Sistemas.

**Curso:** Programación.

**Código del curso:** 213023.

## 12. Conclusión

El desarrollo de Sistema de gestion de clientes permite integrar diferentes conceptos de programación mediante la construcción de un sistema orientado a la gestión de clientes, servicios y reservas.

A través de este ejercicio se fortalece la comprensión de la programación orientada a objetos, especialmente en el uso de clases abstractas, herencia, encapsulamiento y polimorfismo. Asimismo, se reconoce la importancia de validar la información y controlar las excepciones para mejorar la organización y confiabilidad de las aplicaciones.

Finalmente, el proyecto constituye una experiencia de aprendizaje que permite aplicar los conocimientos adquiridos en el curso de Programación de la UNAD, acercando los fundamentos teóricos a una situación práctica de desarrollo de software.
