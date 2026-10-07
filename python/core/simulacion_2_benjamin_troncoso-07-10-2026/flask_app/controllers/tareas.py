from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.tarea import Tarea
from flask_app.models.categoria import Categoria

@app.route('/tareas')
def dashboard():
    if 'user_id' not in session: return redirect('/')
    filtros = {
        'busqueda': request.args.get('busqueda', ''),
        'estado': request.args.get('estado', 'Todos'),
        'prioridad': request.args.get('prioridad', 'Todas')
    }
    user_id = session['user_id']
    return render_template('panel.html', 
                           tareas=Tarea.get_all_by_user(user_id, filtros),
                           proximas=Tarea.get_upcoming_by_user(user_id),
                           resumen=Tarea.get_resumen_by_user(user_id),
                           categorias=Categoria.get_all_by_user(user_id),
                           filtros=filtros)

@app.route('/tareas/nueva')
def nueva_tarea():
    if 'user_id' not in session: return redirect('/')
    return render_template('tarea_nueva.html', categorias=Categoria.get_all_by_user(session['user_id']))

@app.route('/tareas/crear', methods=['POST'])
def crear_tarea():
    if 'user_id' not in session: return redirect('/')
    if not Tarea.validate_task(request.form): return redirect('/tareas/nueva')
    Tarea.save({**request.form, "user_id": session['user_id']})
    return redirect('/tareas')

@app.route('/tareas/<int:task_id>')
def detalle_tarea(task_id):
    if 'user_id' not in session: return redirect('/')
    tarea = Tarea.get_by_id(task_id)
    if not tarea or tarea.user_id != session['user_id']: return redirect('/tareas')
    return render_template('tarea_detalle.html', tarea=tarea)

@app.route('/tareas/editar/<int:task_id>')
def editar_tarea(task_id):
    if 'user_id' not in session: return redirect('/')
    tarea = Tarea.get_by_id(task_id)
    if not tarea or tarea.user_id != session['user_id']: return redirect('/tareas')
    return render_template('tarea_editar.html', tarea=tarea, categorias=Categoria.get_all_by_user(session['user_id']))

@app.route('/tareas/actualizar/<int:task_id>', methods=['POST'])
def actualizar_tarea(task_id):
    if 'user_id' not in session: return redirect('/')
    tarea = Tarea.get_by_id(task_id)
    if not tarea or tarea.user_id != session['user_id']: return redirect('/tareas')
    if not Tarea.validate_task(request.form): return redirect(f'/tareas/editar/{task_id}')
    Tarea.update({**request.form, "id": task_id})
    return redirect('/tareas')

@app.route('/tareas/estado/<int:task_id>/<string:estado>')
def cambiar_estado(task_id, estado):
    if 'user_id' not in session: return redirect('/')
    tarea = Tarea.get_by_id(task_id)
    if tarea and tarea.user_id == session['user_id']:
        Tarea.update_estado(task_id, estado)
    return redirect('/tareas')

@app.route('/tareas/borrar/<int:task_id>')
def borrar_tarea(task_id):
    if 'user_id' not in session: return redirect('/')
    tarea = Tarea.get_by_id(task_id)
    if tarea and tarea.user_id == session['user_id']:
        Tarea.delete(task_id)
    return redirect('/tareas')