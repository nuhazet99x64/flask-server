from data.producto import productos
from flask import Flask, render_template, request, url_for

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


@app.route("/contacto", methods=["POST"])
def contacto_post():
    nombre = request.form.get("nombre")
    mensaje = request.form.get("mensaje")
    return render_template("contacto-data.html", nombre=nombre, mensaje=mensaje)


@app.route("/contacto", methods=["GET"])
def contacto_get():
    return render_template("contacto.html")


@app.route("/filtrar")
def filtrar():
    return render_template("filtrar.html")


@app.route("/filtrar-data", methods=["GET"])
def filtrar_data():
    precio_min = request.args.get("precio_min", type=float)
    precio_max = request.args.get("precio_max", type=float)
    print(f"Precio minimo: {precio_min}")
    print(f"Precio maximo: {precio_max}")
    productos_filtrados = [
        producto
        for producto in productos
        if precio_min <= producto["precio"] <= precio_max
    ]
    print(f"Productos filtrados: {productos_filtrados}")
    return render_template(
        "catalogo.html", nombre="algo", lista_productos=productos_filtrados
    )


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
