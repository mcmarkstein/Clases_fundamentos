from flask import Flask

app = Flask(__name__)   #esto se usa simepre


@app.route("/", methods=['GET']) #esto es una annotation, definimos una ruta, y luego el metodo http
def hello_world():
    return "<p>Hello, World!</p>"

#en postman -->  http://localhost:5000