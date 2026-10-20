# Importar Blueprint y funciones de renderizado
from flask import Blueprint, render_template, redirect, request, session
from flask_app.models.entrada import Entrada

# Definir el Blueprint para entradas
entradas_bp = Blueprint('entradas', __name__)

# Ruta del dashboard principal
@entradas_bp.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')
    entradas = Entrada.obtener_por_usuario(session['usuario_id'])
    return render_template('dashboard.html', entradas=entradas)

# Ruta para la vista de nueva entrada
@entradas_bp.route('/nuevo')
def nueva_entrada():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('nueva_entrada.html')

# Ruta para crear una entrada en la BD
@entradas_bp.route('/crear', methods=['POST'])
def crear_entrada():
    if 'usuario_id' not in session:
        return redirect('/')
    if not Entrada.validar_entrada(request.form):
        return redirect('/nuevo')
    
    data = {
        "fecha_entrada": request.form['fecha_entrada'],
        "notas": request.form['notas'],
        "usuario_id": session['usuario_id']
    }
    Entrada.guardar(data)
    return redirect('/dashboard')

# Ruta para ver una entrada específica
@entradas_bp.route('/ver/<int:id>')
def ver_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')
    entrada = Entrada.obtener_por_id(id)
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')
    return render_template('ver_entrada.html', entrada=entrada)

# Ruta para el editor de entradas
@entradas_bp.route('/editor/<int:id>')
def editar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')
    entrada = Entrada.obtener_por_id(id)
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')
    return render_template('editar_entrada.html', entrada=entrada)

# Ruta para actualizar una entrada
@entradas_bp.route('/actualizar/<int:id>', methods=['POST'])
def actualizar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')
    entrada = Entrada.obtener_por_id(id)
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')
    if not Entrada.validar_entrada(request.form):
        return redirect(f'/editor/{id}')
    
    data = {
        "id": id,
        "fecha_entrada": request.form['fecha_entrada'],
        "notas": request.form['notas']
    }
    Entrada.actualizar(data)
    return redirect('/dashboard')

# Ruta para borrar una entrada
@entradas_bp.route('/borrar/<int:id>')
def borrar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')
    entrada = Entrada.obtener_por_id(id)
    if entrada and entrada.usuario_id == session['usuario_id']:
        Entrada.eliminar(id)
    return redirect('/dashboard')

# Ruta para buscar entradas
@entradas_bp.route('/buscar/<termino>')
def buscar(termino):
    if 'usuario_id' not in session:
        return redirect('/')
    entradas = Entrada.buscar_por_termino(termino, session['usuario_id'])
    return render_template('buscar.html', entradas=entradas, termino=termino)

# Ruta para procesar el formulario de búsqueda
@entradas_bp.route('/buscar_redirect', methods=['POST'])
def buscar_redirect():
    if 'usuario_id' not in session:
        return redirect('/')
    termino = request.form['termino']
    return redirect(f'/buscar/{termino}')