from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    """ Ruta raíz: Muestra el formulario de inicio de sesión y registro """
    if 'user_id' in session:
        return redirect('/libros')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    """ Procesa el registro de un nuevo usuario en la plataforma """
    if not Usuario.validate_register(request.form):
        return redirect('/')
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        # Generamos el hash seguro de la contraseña con bcrypt
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = Usuario.save(data)
    
    # Iniciamos sesión automáticamente guardando los datos en la sesión
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    return redirect('/libros')

@app.route('/login', methods=['POST'])
def login():
    """ Valida las credenciales e inicia sesión para un usuario existente """
    user = Usuario.get_by_email({'email': request.form['email']})
    if not user:
        flash("Correo electrónico no encontrado.", "login")
        return redirect('/')
        
    # Comparamos la contraseña ingresada con el hash guardado en la BD
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Contraseña incorrecta.", "login")
        return redirect('/')
    
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    return redirect('/libros')

@app.route('/logout')
def logout():
    """ Cierra la sesión del usuario actual limpiando la memoria de sesión """
    session.clear()
    return redirect('/')