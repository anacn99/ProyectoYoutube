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

Una vez construído todo el proceso podemos hacer el docker run para ver como se ejecuta:
~~~
(venv) asir2a@perlanegra13:~/Documentos/SRI/Pruebas SRI/ProyectoYoutube$ docker-compose run python
Creating proyectoyoutube_python_run ... done
Title:  Samantha Hudson y Papa Topo - Por España
Number of views:  1264075
Length of video:  266 seconds
Description:  Samantha Hudson y Papa Topo - Por España
https://links.altafonte.com/ox8plxd
~~~

Hemos creado además un archivo de docker-compose.yml, que es el que lanzaremos con la imagen para lanzar el script de python que contiene lo que queremos.
Nuestro script de python se llama "miscript.py".
~~~
    services:
        python:
            image: youtubeimagen:latest
            volumes:
                - ./app:/usr/src/app
            stdin_open: true
            tty: true
            command: [ "python", "miscript.py"]
~~~
Hemos creado el archivo en el que hemos mapeado las carpetas que contendran la información que necesitamos.En este caso , una carpeta app.
Para poder descargarnos un vídeo de Youtube, que es el objetivo de esta tarea de python, necesitamos en concreto la librería de pytube. Y realizamos el script de la siguiente manera:
~~~

from pytube import YouTube

#link = input("Enter the link: ")
yt = YouTube("https://www.youtube.com/watch?v=Amx9AXllumY&ab_channel=SamanthaHudson")

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)


yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
~~~
Con este script nos descargará el vídeo de youtube que hayamos enlaceado, nos realizará esa descarga en el mismo directorio donde tenemos el script guardado.

Sin embargo para poder realizar esto, necesitamos descargar la librería de pytube, ya que solo hemos instalado python. Creamos el archivo de Dockerfile que contendrá los siguientes comandos:
~~~
FROM python:3

WORKDIR /usr/src/app

RUN pip install pytube

COPY  ./app /usr/src/app

CMD [ "python", "miscript.py"]
~~~
En principio todos los archivos necesarios para levantar el docker-compose con pytube están listos. Ahora nos queda realizar el docker-compose up para levantar el contenedor que lanzará el script.
~~~
(venv) asir2a@perlanegra13:~/Documentos/SRI/Pruebas SRI/ProyectoYoutube$ docker-compose up
Recreating proyectoyoutube_python_1 ... done
Attaching to proyectoyoutube_python_1
python_1  | Title:  Samantha Hudson y Papa Topo - Por España
python_1  | Number of views:  1264071
python_1  | Length of video:  266 seconds
python_1  | Description:  Samantha Hudson y Papa Topo - Por España
python_1  | https://links.altafonte.com/ox8plxd
.....
~~~
Yendo al directorio correspondiente podemos ver que se ha creado el vídeo.

Ahora podemos subir esta imagen que hemos creado al servicio de DockerHub.
Para ello nos creamos la cuenta y realizamos los pasos que nos indican.Creamos el repositorio,le damos un nombre y desde la terminal hacemos lo siguiente:
~~~
  docker login
  
  docker tag youtubeimagen anacn99/python-youtube1
  
  docker push anacn99/python-youtube1:latest
~~~
  El enlace de nuestro repositorio para dockerhub es el siguiente:
[enlace a docker](https://hub.docker.com/repositories/anacn99)
    
  
