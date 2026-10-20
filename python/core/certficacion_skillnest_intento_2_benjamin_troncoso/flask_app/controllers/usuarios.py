# Importar Flask, Blueprint y herramientas necesarias
from flask import Blueprint, render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt
from flask_app import app

# Definir el Blueprint para usuarios
usuarios_bp = Blueprint('usuarios', __name__)
bcrypt = Bcrypt(app)

# Ruta principal (registro y login)
@usuarios_bp.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el registro
@usuarios_bp.route('/registro', methods=['POST'])
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

# Ruta para procesar el inicio de sesión
@usuarios_bp.route('/login', methods=['POST'])
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

# Ruta para cerrar sesión
@usuarios_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Ruta de validación para rutas perdidas (Catch-all)
@usuarios_bp.route('/<path:path>', methods=['GET', 'POST'])
def ruta_perdida(path):
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return redirect('/')