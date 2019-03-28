from webbrowser import open_new_tab
import json,requests
response = requests.get("http://jsonplaceholder.typicode.com/photos")
fotos = json.loads(response.content)

nombreArchivo = 'index.html'
Archivo = open(nombreArchivo, 'w')

mensaje = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="estilo.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <title>Document</title>
</head>
<body>
    <div class="header">
        <h1>LSV TEAM</h1>
    </div>

    <div class="padre">
      <div>
        <h2>Fotos</h2>
      </div>"""
agregador=""
for foto in fotos[0:10]:
        agregador+="""
        <div class="hijo">
                <img class="img" src="{}" alt="{}">
        </div>""".format(foto['url'],foto['title'])
mensaje+=agregador+'\n          </div>'

mensaje+="""
    <center><div class="contenedor1" style="width: 98%">
      <table class="table table-dark">
          <div>
              <br><br>
              <h2>Users</h2>
          </div>
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Name</th>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
            </tr>
          </thead>
          <tbody>
"""
response = requests.get("http://jsonplaceholder.typicode.com/users")
users = json.loads(response.content)
agregador=""
for user in users[0:10]:
        agregador+="""
            <tr>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
            </tr>""".format(user['id'],user['name'],user['username'],user['email'])
mensaje+=agregador+"""
          </tbody>
      </table>
    </div></center>
    <center><div class="contenedor1" style="width: 98%">
      <table class="table table-dark">
          <div>
              <br><br>
              <h2>Todos</h2>
          </div>
          <thead>
            <tr>
              <th scope="col">UserId</th>
              <th scope="col">Id</th>
              <th scope="col">Title</th>
              <th scope="col">Completed</th>
            </tr>
          </thead>
          <tbody>"""

response = requests.get("http://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.content)
agregador=""
for todo in todos[0:10]:
        agregador+="""
            <tr>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
            </tr>""".format(todo['userId'],todo['id'],todo['title'],todo['completed'])
mensaje+=agregador+"""
          </tbody>
      </table>
    </div></center>
    <center><div class="contenedor1" style="width: 98%">
      <table class="table table-dark">
          <div>
              <br><br>
              <h2>Comments</h2>
          </div>
          <thead>
            <tr>
                <th scope="col">PostId</th>
                <th scope="col">Id</th>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Body</th>
            </tr>
          </thead>
          <tbody>"""

response = requests.get("http://jsonplaceholder.typicode.com/comments")
comments = json.loads(response.content)
agregador=""
for comment in comments[0:10]:
        agregador+="""
            <tr>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
                <td>{}</td>
            </tr>""".format(comment['postId'],comment['id'],comment['name'],comment['email'],comment['body'])
mensaje+=agregador+"""
          </tbody>
      </table>
    </div></center>
</body>
</html>"""


open_new_tab(nombreArchivo)

Archivo.write(mensaje)
Archivo.close()
