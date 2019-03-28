from http.server import HTTPServer, BaseHTTPRequestHandler
import os
rutas={}
for i in os.listdir('.'):
    rutas.setdefault('/{}'.format(i.split('.')[0]),i)
print(rutas)
class StaticServer(BaseHTTPRequestHandler):
    def do_GET(self):
        root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Servidor_Estatico')
        if self.path in rutas.keys():
            content = self.handle_http(200, 'text/html')
            self.wfile.write(content)
        else:
            content = self.handle_http(404, 'text/html')
            self.wfile.write(content)
    def handle_http(self,status,conten_type):
        self.send_response(status)
        self.end_headers()
        if status == 200:
            routes_contect = rutas[self.path]
            f = open(routes_contect, 'r')
        elif status == 404:
            f = open('error.html', 'r')
        return bytes(f.read(), 'UTF-8')

def run(server_class, handler_class, port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Servidor en el puerto {}".format(port))
    httpd.serve_forever()

def indexoff():
    nombreArchivo = 'index.html'
    Archivo = open(nombreArchivo, 'w')

    mensaje = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>"""
    agregador=""
    for i in rutas:
        agregador+="""
            <a style="text-decoration:none" href="{}">{}</a><br>
        """.format(i,i.split('/')[1])
    mensaje += agregador + """
    </body>
    </html>"""
    Archivo.write(mensaje)
    Archivo.close()
    rutas.setdefault('/','index.html')

port=''
while not port or not port.isnumeric():
    port = input('Digite el puerto donde abrira el Servidor Web: ')

port = int(port)
indexoff()
run(HTTPServer,StaticServer,port)
