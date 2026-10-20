from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.entrada import Entrada

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')
    entradas = Entrada.obtener_por_usuario(session['usuario_id'])
    return render_template('dashboard.html', entradas=entradas)

@app.route('/nuevo')
def nueva_entrada():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('nueva_entrada.html')

@app.route('/crear', methods=['POST'])
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

@app.route('/ver/<int:id>')
def ver_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')
    entrada = Entrada.obtener_por_id(id)
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')
    return render_template('ver_entrada.html', entrada=entrada)

@app.route('/editor/<int:id>')
def editar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')
    entrada = Entrada.obtener_por_id(id)
    if not entrada or entrada.usuario_id != session['usuario_id']:
        return redirect('/dashboard')
    return render_template('editar_entrada.html', entrada=entrada)

@app.route('/actualizar/<int:id>', methods=['POST'])
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

@app.route('/borrar/<int:id>')
def borrar_entrada(id):
    if 'usuario_id' not in session:
        return redirect('/')
    entrada = Entrada.obtener_por_id(id)
    if entrada and entrada.usuario_id == session['usuario_id']:
        Entrada.eliminar(id)
    return redirect('/dashboard')

@app.route('/buscar/<termino>')
def buscar(termino):
    if 'usuario_id' not in session:
        return redirect('/')
    entradas = Entrada.buscar_por_termino(termino, session['usuario_id'])
    return render_template('buscar.html', entradas=entradas, termino=termino)

@app.route('/buscar_redirect', methods=['POST'])
def buscar_redirect():
    if 'usuario_id' not in session:
        return redirect('/')
    termino = request.form['termino']
    return redirect(f'/buscar/{termino}')