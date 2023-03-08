# ProyectoYoutube

## Docker + Python

Comenzamos el proceso descargando la imagen de python, ya que la necesitaremos para poder realizar la tarea.
~~~
  docker pull python:3
~~~
Tendremos también que construir la imagen, para ello utilizamos el comando build y le damos el nombre a la imagen:
~~~
  docker build -t youtubeimagen:latest .
~~~ 
~~~
![Texto alternativo](1234.png)
~~~
Hemos creado además un archivo de docker-compose.yml, que es el que lanzaremos con la imagen para lanzar el script de python que contiene lo que queremos.
Nuestro script de python se llama "miscript.py".
~~~
![Texto alternativo](eldockercom.png)
~~~
Hemos creado el archivo en el que hemos mapeado las carpetas que contendran la información que necesitamos.En este caso , una carpeta app.
Para poder descargarnos un vídeo de Youtube, que es el objetivo de esta tarea de python, necesitamos en concreto la librería de pytube. Y realizamos el script de la siguiente manera:
~~~
![Texto alternativo](miscript.png)
~~~
Con este script nos descargará el vídeo de youtube que hayamos enlaceado, nos realizará esa descarga en el mismo directorio donde tenemos el script guardado.

Sin embargo para poder realizar esto, necesitamos descargar la librería de pytube, ya que solo hemos instalado python. Creamos el archivo de Dockerfile que contendrá los siguientes comandos:
~~~
![Texto alternativo](dokcerfile.png)
~~~
En principio todos los archivos necesarios para levantar el docker-compose con pytube están listos. Ahora nos queda realizar el docker-compose up para levantar el contenedor que lanzará el script.
~~~
![Texto alternativo](dockercomposeuppython.png)
~~~
Yendo al directorio correspondiente podemos ver que se ha creado el vídeo:
~~~
![Texto alternativo](comprobarpython.png)
~~~
Ahora podemos subir esta imagen que hemos creado al servicio de DockerHub.
Para ello nos creamos la cuenta y realizamos los pasos que nos indican.Creamos el repositorio,le damos un nombre y desde la terminal hacemos lo siguiente:
~~~
  docker login
  
  docker tag youtubeimagen anacn99/python-youtube1
  
  docker push anacn99/python-youtube1:latest
~~~
  El enlace de nuestro repositorio para dockerhub es el siguiente:
[enlace a docker](https://hub.docker.com/repositories/anacn99)
    
  
