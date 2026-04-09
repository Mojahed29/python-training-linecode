import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {"message": "Hello World!"}

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(HelloWorld())