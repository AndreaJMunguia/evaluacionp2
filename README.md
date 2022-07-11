# Evaluación parte 2: Python
### ESTRUCTURA
Dentro del proyecto podremos encontrar cuatro arhivos diferentes, cada uno con diferente propósito:
1. txt-to-json.py: este archivo se encarga de leer el archio .txt y convertirlo a formato JSON
2. empleados.txt: contiene los datos que se deberán enviar a la base de datos
3. empleados.json: es el archivo resultante de la ejecución del archivo txt-to-json.py
4. request.py: se encarga de enviar el archivo JSON mediante POST a nuestra aplicación Java Spring

### REQUERIMIENTOS 
* Instalación de request, mediante el comando pip install requests
* Instalación de JSON, mediante el comando pip install json

### EJECUCIÓN
1. Ejecutamos nuestro archivo txt-to-json.py para poder obtener nuestro JSON
2. Ejecutamos nuestro proyecto Java Spring en el IDE de nuestra preferencia
3. Ahora ejecutamos el archivo request.py que mediante la dirección http://localhost:8080/apiv1/employee/addemployee enviará los datos a la aplicación Java Spring
4. Ingresamos nuevamente a nuestra BD mediante el url http://localhost:8080/h2-console/ y al hacer SELECT en nuestra tablas podremos observar los datos que en un principio estaban en el archivo .txt

#### AUTOR
Andrea Sarai Juárez Munguia



**NOTA:**  Falta termina bien la conversión de txt a json, para hacer el envio de datos correctamente.
