# flask-cherrypy-dockerized
This is a minimal example of a Flask app running upon CherryPy's WSGI Server.

## Steps to reproduce:

    sudo docker build -t <reponame>:<tag> .
    ... get a coffee
    sudo docker run -d -p <localport>:80 --name <test> <reponame>:<tag>

Then browser to (e.g.) 127.0.0.1:your_local_port

