from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/libros')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    return redirect('/libros')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email({'email': request.form['email']})
    if not user:
        flash("Correo electrónico no encontrado.", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Contraseña incorrecta.", "login")
        return redirect('/')
    
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    return redirect('/libros')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')