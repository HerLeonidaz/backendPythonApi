# Backend

## Ejercicio de backend
Este ejercicio es para que puedas definir qué tecnología de backend te interesa y que nosotros podamos conocer un poco más sobre tu perfil y habilidades.

### Ejercicio 1
Desarrollar un endpoint POST que reciba un json con los siguientes datos:
- Nombre.
- Correo.
- cuantos kilometros caminas a la semana.

Si la persona camina más de 4 kilometros a la semana se deben de registrar los datos en una base de datos (la que sea) y si camina menos de 4 kilometros a la semana le debe de regresar un mensaje "Debes de caminar más".

### Ejercicio 2
Desarrollar un endpoint GET que te traiga todos los registros de la base de datos.

## Desarrollo
lo primero que se hace es crear un entorno virtual con python 3 y activarlo

~~~
python3 -m venv env
~~~
Entrar al directorio env/scripts y ejecutar en el terminal el comando 

~~~
activate
~~~
se deben instalar las dependencias necesarias

~~~
pip install flask
pip install psycopg2-binary
pip install Flask-SQLAlchemy
pip instal request

~~~
## Base de datos 
Como base de datos se usa postgresql 
debes de crear una base de datos 
~~~
CREATE DATABASE api
~~~ 
La api necesita realizar la conexión con la base de datos, en el archivo config.py se debe de hacer las configuraciones necesarias.

Una vez que se tiene el ambiente virtual activo 
y la base de datos 
ejecutar la aplicación desde consola

~~~
python3 main.py
~~~

en el navegador ingresar a la direccion 

~~~
http://localhost:5000/api/v1/persons
~~~

como no hay personas no muestra nada en la respuesta

para probar cuando se recibe un json 

se agregó el archivo python Cliente.py

donde se puede modificar el número de km caminados. 


