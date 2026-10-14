# ==========================================
# SECCIÓN: IMPORTACIONES Y DEPENDENCIAS
# ==========================================
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.cine import Pelicula
from flask_app.config.mysqlconnection import connectToMySQL

# ==========================================
# SECCIÓN: PANEL PRINCIPAL (DASHBOARD DE CINE)
# ==========================================
@app.route('/cine')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    peliculas = Pelicula.obtener_todas()
    return render_template('dashboard.html', peliculas=peliculas)

# ==========================================
# SECCIÓN: VISTA PARA CREAR NUEVA PELÍCULA
# ==========================================
@app.route('/cine/nueva')
def nueva_pelicula():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('nueva_pelicula.html')

# ==========================================
# SECCIÓN: PROCESO DE CREACIÓN DE PELÍCULA
# ==========================================
@app.route('/cine/crear', methods=['POST'])
def crear_pelicula():
    if 'user_id' not in session:
        return redirect('/')
    
    if not Pelicula.validar_pelicula(request.form):
        return redirect('/cine/nueva')
        
    data = {
        "nombre_peli": request.form['nombre_peli'],
        "director": request.form['director'],
        "fecha_estreno": request.form['fecha_estreno'],
        "sinopsis": request.form['sinopsis'],
        "usuario_id": session['user_id']
    }
    
    try:
        Pelicula.guardar(data)
    except Exception:
        flash("El nombre de la película debe ser único.", "pelicula")
        return redirect('/cine/nueva')
        
    return redirect('/cine')

# ==========================================
# SECCIÓN: VER DETALLE DE PELÍCULA Y COMENTARIOS
# ==========================================
@app.route('/cine/<int:id>')
def ver_pelicula(id):
    if 'user_id' not in session:
        return redirect('/')
    pelicula = Pelicula.obtener_por_id({'id': id})
    
    # Obtener comentarios asociados
    query = "SELECT comentarios.*, CONCAT(usuarios.nombre, ' ', usuarios.apellido) as autor FROM comentarios JOIN usuarios ON comentarios.usuario_id = usuarios.id WHERE pelicula_id = %(id)s;"
    comentarios = connectToMySQL(Pelicula.db).query_db(query, {'id': id})
    
    return render_template('ver_pelicula.html', pelicula=pelicula, comentarios=comentarios)

# ==========================================
# SECCIÓN: VISTA PARA EDITAR PELÍCULA
# ==========================================
@app.route('/cine/editar/<int:id>')
def editar_pelicula(id):
    if 'user_id' not in session:
        return redirect('/')
    pelicula = Pelicula.obtener_por_id({'id': id})
    if pelicula.usuario_id != session['user_id']:
        return redirect('/cine')
    return render_template('editar_pelicula.html', pelicula=pelicula)

# ==========================================
# SECCIÓN: PROCESO DE ACTUALIZACIÓN DE PELÍCULA
# ==========================================
@app.route('/cine/actualizar/<int:id>', methods=['POST'])
def actualizar_pelicula(id):
    if 'user_id' not in session:
        return redirect('/')
    
    if not Pelicula.validar_pelicula(request.form):
        return redirect(f'/cine/editar/{id}')
        
    data = {
        "id": id,
        "nombre_peli": request.form['nombre_peli'],
        "director": request.form['director'],
        "fecha_estreno": request.form['fecha_estreno'],
        "sinopsis": request.form['sinopsis']
    }
    Pelicula.actualizar(data)
    return redirect('/cine')

# ==========================================
# SECCIÓN: ELIMINACIÓN DE PELÍCULA
# ==========================================
@app.route('/cine/borrar/<int:id>')
def borrar_pelicula(id):
    if 'user_id' not in session:
        return redirect('/')
    pelicula = Pelicula.obtener_por_id({'id': id})
    if pelicula and pelicula.usuario_id == session['user_id']:
        Pelicula.eliminar({'id': id})
    return redirect('/cine')

# ==========================================
# SECCIÓN: AGREGAR COMENTARIO A PELÍCULA
# ==========================================
@app.route('/comentar/<int:pelicula_id>', methods=['POST'])
def agregar_comentario(pelicula_id):
    if 'user_id' not in session:
        return redirect('/')
    
    pelicula = Pelicula.obtener_por_id({'id': pelicula_id})
    # BONUS: Un usuario no puede comentar su propia película
    if pelicula.usuario_id == session['user_id']:
        flash("Un usuario no puede comentar su propia película.", "comentario")
        return redirect(f'/cine/{pelicula_id}')
        
    query = "INSERT INTO comentarios (comentario, usuario_id, pelicula_id) VALUES (%(comentario)s, %(usuario_id)s, %(pelicula_id)s);"
    data = {
        "comentario": request.form['comentario'],
        "usuario_id": session['user_id'],
        "pelicula_id": pelicula_id
    }
    connectToMySQL(Pelicula.db).query_db(query, data)
    return redirect(f'/cine/{pelicula_id}')