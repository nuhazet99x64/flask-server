from flask import Flask, render_template

# Inicializamos la aplicación
app = Flask(__name__)


# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
    # return """
    #     <h1>¡Hola desde Flask en Docker!!!!</h1>
    #     <p>Este es tu primer servidor Python funcionando.</p>
    # """
    return render_template("index.html")


@app.route("/saludo/amigo")
def saludo():
    return render_template("saludo.html")


@app.route("/multiplicar/<int:num1>/<int:num2>")
def multiplicar(num1, num2):
    return f"<h1>Multiplicar {num1} x {num2} es {num1 * num2}</h1>"


@app.route("/catalogo/<int:id_producto>")
def catalogo(id_producto):
    productos = [
        {"nombre": "Teclado Mecánico", "precio": 49.99, "disponible": True},
        {"nombre": "Ratón Óptico", "precio": 19.99, "disponible": False},
        {"nombre": "Monitor 4K", "precio": 299.99, "disponible": True},
    ]
    return render_template(
        "catalogo.html",
        nombre="algo",
        id_producto=id_producto,
        lista_productos=productos,
    )


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
