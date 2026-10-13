from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.categoria import Categoria

@app.route('/categorias')
def categorias():
    if 'user_id' not in session: 
        return redirect('/')
    print(">>> Usuario actual en sesión:", session['user_id'])
    return render_template('categorias.html', categorias=Categoria.get_all_by_user(session['user_id']))

@app.route('/categorias/nueva')
def nueva_categoria():
    if 'user_id' not in session: 
        return redirect('/')
    return render_template('categoria_nueva.html')

@app.route('/categorias/crear', methods=['POST'])
def crear_categoria():
    if 'user_id' not in session: 
        return redirect('/')
    
    # Validar solo que el nombre tenga al menos 3 caracteres
    if len(request.form['nombre']) < 3:
        flash("El nombre debe tener al menos 3 caracteres.", "category")
        return redirect('/categorias/nueva')
    
    # Guardar directamente vinculado al usuario activo de la sesión
    Categoria.save({
        "nombre": request.form['nombre'],
        "user_id": session['user_id']
    })
    
    return redirect('/categorias')

@app.route('/categorias/borrar/<int:category_id>')
def borrar_categoria(category_id):
    if 'user_id' not in session: 
        return redirect('/')
    categoria = Categoria.get_by_id(category_id)
    if categoria and categoria.user_id == session['user_id']:
        Categoria.delete(category_id)
    return redirect('/categorias')