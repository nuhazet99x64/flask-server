from flask import Flask, render_template, url_for

# Inicializamos la aplicación
app = Flask(__name__)

productos = [
    {"nombre": "Teclado Mecánico", "precio": 49.99, "disponible": True},
    {"nombre": "Ratón Óptico", "precio": 19.99, "disponible": False},
    {"nombre": "Monitor 4K", "precio": 299.99, "disponible": True},
]


# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
    # return """
    #     <h1>¡Hola desde Flask en Docker!!!!</h1>
    #     <p>Este es tu primer servidor Python funcionando.</p>
    # """
    return render_template("index.html")


@app.route("/saludo/<name>")
def saludo(name):
    return render_template("saludo.html", name=name)


@app.route("/multiplicar/<int:num1>/<int:num2>")
def multiplicar(num1, num2):
    return f"<h1>Multiplicar {num1} x {num2} es {num1 * num2}</h1>"


@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", nombre="algo", lista_productos=productos)


@app.route("/catalogo/<int:idProducto>")
def producto(idProducto):
    return render_template(
        "producto.html", idProducto=idProducto, producto=productos[idProducto]
    )


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
