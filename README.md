# Implementación de un chat sencillo con una arquitectura de 4 capas
Universidad del Valle de Guatemala 
Laboratorio 02  - Redes  

## Description

Actualmente, las empresas o instituciones tienen errores en todo tipo de comunicación, y constantemente buscamos innovar en los sistemas que se encargan de implementar algoritmos que detectan los errores y nos permitan manejar de forma adecuada las fallas o poder identificarlas previo a que puedan ocurrir. Por lo tanto, a lo largo de la evolución del internet se han desarrollado distintos mecanismos que sirven tanto para la detención como para la corrección de los errores. 
Debido a esto, es importante que, como programadores, comprendamos en que momento pueden existir errores en la transferencia de mensajes dentro de una arquitectura de un modelo de capas. 


Durante la práctica de laboratorio se elabora un modelo básico de implementación del intercambio de mensajes entre un cliente y un servidor. Para poder elaborar el modelo debemos de conocer la arquitectura que debemos de implementar. Dicha arquitectura es el modelo de 4 Capas propuesto en la práctica de laboratorio. 
Dicho modelo de capas consiste en lo siguiente: 
•	Emisor 
  o (1)	Aplicación 
  o	(2) Verificación 
  o	(3) Ruido 
  o	(4) Transferencia 

•	Receptor 
 o	(4) Transmisión 
 o	(3) Codificación 
 o	(2) Verificación 
 o	(1) Aplicación 
 
 
Al implementar nuestro algoritmo debemos de cumplir con los siguientes objetivos: 

•	Identificar ventajas y desventajas de implementación para la detección y corrección de errores 
•	Comprender los elementos de una arquitectura de capas 

Para poder llevar a cabo la implementación de nuestro laboratorio se establece un desarrollo por 3 fases la primera comprende en el desarrollo de la arquitectura para envío y recepción de mensajes, la segunda comprende en la implementación de los algoritmos que vamos a analizar: Corrección y detección de errores y la tercera fase comprende en el análisis de pruebas de algoritmos implementados. 


## Getting Started

### Dependencies

* Python 3.9.6

### Installing

* Se deberá de tener dos terminales para poder utilizar el programa. 
* Se puede modular con una máquina virtual y correr el archivo que corresponde al cliente y al servidor en lugares distintos 
* Es importante poder visualizar todo el tiempo la implementación del cliente y el servidor  

### Executing program

Para poder ejecutar el programa deberá de tener dos terminales. A continuación se describe que procedimiento debe de efectuar para poder comprobar el funcionamiento del programa. 

* Abrir terminal 1 (cmd) 
* Introducir: 
```
py server_side.py
```
* Abrir terminal 2 (cmd) 
* Introducir: 
```
py client_side.py
ingresar cadena de caracteres. Por ejemplo: Hola Mundo 
```
Al momento de ingresar la cadena, podrá ver la interacción en la terminal del servidor. 

## Authors

Elaborado por: Grupo 2 

* María Mercedes Retolaza
* Cesar Rodas 
