from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/tareas')
    return render_template('inicio.html')

@app.route('/registro', methods=['POST'])
def registro():
    if not Usuario.validate_register(request.form):
        return redirect('/')
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = Usuario.save(data)
    session['user_id'] = user_id
    session['user_nombre'] = request.form['nombre']
    return redirect('/tareas')

@app.route('/login', methods=['POST'])
def login():
    user = Usuario.get_by_email(request.form['email'])
    if not user or not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Credenciales incorrectas.", "login")
        return redirect('/')
    session['user_id'] = user.id
    session['user_nombre'] = user.nombre
    return redirect('/tareas')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')