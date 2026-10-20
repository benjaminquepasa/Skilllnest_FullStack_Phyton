from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    if not Usuario.validar_registro(request.form):
        return redirect('/')
    
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "edad": request.form['edad'],
        "password": password_hash
    }
    usuario_id = Usuario.guardar(data)
    session['usuario_id'] = usuario_id
    session['nombre_usuario'] = request.form['nombre']
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.obtener_por_email(request.form['email'])
    if not usuario:
        flash("El email debe estar registrado en BD.", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("La contraseña debe ser la correspondiente a la BD.", "login")
        return redirect('/')
    
    session['usuario_id'] = usuario.id
    session['nombre_usuario'] = usuario.nombre
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')