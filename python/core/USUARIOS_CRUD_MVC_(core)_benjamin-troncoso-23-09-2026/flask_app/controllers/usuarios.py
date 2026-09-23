from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.usuario import Usuario

@app.route("/usuarios")
def usuarios():
    todos_usuarios = Usuario.get_all()
    return render_template("index.html", usuarios=todos_usuarios)

@app.route("/usuarios/nuevo")
def nuevo():
    return render_template("nuevo.html")

@app.route("/usuarios/crear", methods=["POST"])
def crear():
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip()
    }

    if not datos["nombre"] or not datos["apellido"] or not datos["email"]:
        return render_template("nuevo.html", error="Todos los campos son obligatorios.", datos=datos)

    resultado = Usuario.save(datos)
    if resultado is False:
        return render_template("nuevo.html", error="No fue posible crear el usuario.", datos=datos)

    return redirect(url_for("usuarios"))

@app.route("/usuarios/<int:id>")
def detalle(id):
    usuario_encontrado = Usuario.get_by_id(id)
    if not usuario_encontrado:
        return "Usuario no encontrado", 404
    return render_template("detalle.html", usuario=usuario_encontrado)

@app.route("/usuarios/editar/<int:id>")
def editar(id):
    usuario_encontrado = Usuario.get_by_id(id)
    if not usuario_encontrado:
        return "Usuario no encontrado", 404
    return render_template("editar.html", usuario=usuario_encontrado)

@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar(id):
    datos = {
        "id": id,
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip()
    }

    if not datos["nombre"] or not datos["apellido"] or not datos["email"]:
        usuario_actual = Usuario.get_by_id(id)
        return render_template("editar.html", usuario=usuario_actual, error="Todos los campos son obligatorios.")

    resultado = Usuario.update(datos)
    if resultado is False:
        usuario_actual = Usuario.get_by_id(id)
        return render_template("editar.html", usuario=usuario_actual, error="No fue posible actualizar el usuario.")

    return redirect(url_for("usuarios"))

@app.route("/usuarios/borrar/<int:id>")
def borrar(id):
    resultado = Usuario.delete(id)
    if resultado is False:
        return "No fue posible eliminar el usuario.", 500
    return redirect(url_for("usuarios"))