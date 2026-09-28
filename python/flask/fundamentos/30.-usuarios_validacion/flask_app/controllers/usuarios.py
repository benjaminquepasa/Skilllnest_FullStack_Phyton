from flask_app import app
from flask import render_template, request, redirect, url_for, session, flash
from flask_app.models.usuario import Usuario
@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    datos_formulario = session.pop("datos_formulario", {})
    return render_template("nuevo_usuario.html", datos_formulario=datos_formulario)
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip()
    data = {"nombre": nombre, "apellido": apellido, "email": email}
    if not Usuario.validar_usuario(data):
        session["datos_formulario"] = data
        return redirect(url_for("nuevo_usuario"))
    if Usuario.email_existe(data["email"]):
        flash("El email ingresado ya está registrado.", "email")
        session["datos_formulario"] = data
        return redirect(url_for("nuevo_usuario"))
    resultado = Usuario.save(data)
    if resultado is False:
        flash("No fue posible crear el usuario.", "error")
        session["datos_formulario"] = data
        return redirect(url_for("nuevo_usuario"))
    session.pop("datos_formulario", None)
    flash("Usuario creado correctamente.", "success")
    return redirect(url_for("usuarios"))