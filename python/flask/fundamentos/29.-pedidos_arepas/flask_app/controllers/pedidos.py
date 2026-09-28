from flask_app import app
from flask import render_template, request, redirect, url_for, flash
from flask_app.models.pedido import Pedido

@app.route("/")
def inicio():
    return redirect(url_for("pedidos"))

@app.route("/pedidos")
def pedidos():
    todos_los_pedidos = Pedido.get_all()
    return render_template("pedidos.html", pedidos=todos_los_pedidos)

@app.route("/pedidos/nuevo")
def nuevo_pedido():
    return render_template("nuevo_pedido.html")

@app.route("/pedidos/crear", methods=["POST"])
def crear_pedido():
    nombre = request.form.get("nombre", "").strip()
    tipo_arepa = request.form.get("tipo_arepa", "").strip()
    cantidad = request.form.get("cantidad", "").strip()

    data = {
        "nombre": nombre,
        "tipo_arepa": tipo_arepa,
        "cantidad": cantidad
    }

    if not Pedido.validar_pedido(data):
        return redirect(url_for("nuevo_pedido"))

    data["cantidad"] = int(data["cantidad"])
    resultado = Pedido.save(data)

    if resultado is False:
        flash("No fue posible guardar el pedido.", "danger")
        return redirect(url_for("nuevo_pedido"))

    flash("Pedido creado correctamente.", "success")
    return redirect(url_for("pedidos"))