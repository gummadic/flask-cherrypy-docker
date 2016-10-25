from cherrypy import wsgiserver
from auth.api import auth
from data.api import data

dispatcher = wsgiserver.WSGIPathInfoDispatcher({'/auth': auth,'/data': data})

server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 80), dispatcher)

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
