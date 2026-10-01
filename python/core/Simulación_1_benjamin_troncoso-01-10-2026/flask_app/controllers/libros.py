from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.libro import Libro

@app.route('/libros')
def dashboard():
    """ Carga la vista principal del panel con los libros propios y de la comunidad """
    if 'user_id' not in session:
        return redirect('/')
    
    all_books = Libro.get_all()
    # Filtramos los libros creados por el usuario conectado
    user_books = [b for b in all_books if b.user_id == session['user_id']]
    # Mostramos todos los libros en la comunidad
    community_books = all_books 
    
    return render_template('panel.html', user_books=user_books, community_books=community_books)

@app.route('/explorar')
def explore():
    """ Carga la vista para explorar todos los libros publicados """
    if 'user_id' not in session:
        return redirect('/')
    all_books = Libro.get_all()
    return render_template('explorar.html', all_books=all_books)

@app.route('/libros/nuevo')
def new_book_page():
    """ Muestra el formulario para registrar un nuevo libro """
    if 'user_id' not in session:
        return redirect('/')
    return render_template('nuevo_libro.html')

@app.route('/libros/crear', methods=['POST'])
def create_book():
    """ Procesa el guardado del nuevo libro en la base de datos """
    if 'user_id' not in session:
        return redirect('/')
    
    if not Libro.validate_book(request.form):
        return redirect('/libros/nuevo')
    
    data = {
        "title": request.form['title'],
        "author": request.form['author'],
        "genre": request.form['genre'],
        "publication_date": request.form['publication_date'],
        "description": request.form['description'],
        "user_id": session['user_id']
    }
    Libro.save(data)
    return redirect('/libros')

@app.route('/libros/<int:id>')
def show_book(id):
    """ Muestra la información detallada de un libro y sus favoritos """
    if 'user_id' not in session:
        return redirect('/')
    
    book = Libro.get_by_id({'id': id})
    users_favorited = Libro.get_users_who_favorited({'book_id': id})
    user_already_favorited = any(u['id'] == session['user_id'] for u in users_favorited)
    
    return render_template('ver_libro.html', book=book, users_favorited=users_favorited, user_already_favorited=user_already_favorited)

@app.route('/libros/editar/<int:id>')
def edit_book_page(id):
    """ Muestra el formulario con los datos actuales para editar un libro """
    if 'user_id' not in session:
        return redirect('/')
    
    book = Libro.get_by_id({'id': id})
    # Aseguramos que solo el autor pueda editar su libro
    if book.user_id != session['user_id']:
        return redirect('/libros')
        
    return render_template('editar_libro.html', book=book)

@app.route('/libros/actualizar/<int:id>', methods=['POST'])
def update_book(id):
    """ Procesa la actualización del libro en la base de datos """
    if 'user_id' not in session:
        return redirect('/')
    
    if not Libro.validate_book(request.form):
        return redirect(f'/libros/editar/{id}')
        
    data = {
        "id": id,
        "title": request.form['title'],
        "author": request.form['author'],
        "genre": request.form['genre'],
        "publication_date": request.form['publication_date'],
        "description": request.form['description']
    }
    Libro.update(data)
    return redirect('/libros')

@app.route('/libros/borrar/<int:id>')
def delete_book(id):
    """ Elimina un libro si pertenece al usuario en sesión """
    if 'user_id' not in session:
        return redirect('/')
    
    book = Libro.get_by_id({'id': id})
    if book and book.user_id == session['user_id']:
        Libro.delete({'id': id})
    return redirect('/libros')

@app.route('/libros/favorito/<int:id>', methods=['POST'])
def add_favorite(id):
    """ Añade un libro a la lista de favoritos del usuario """
    if 'user_id' not in session:
        return redirect('/')
    
    Libro.add_to_favorites({'user_id': session['user_id'], 'book_id': id})
    return redirect(f'/libros/{id}')

@app.route('/favoritos')
def favorites_page():
    """ Muestra la vista con todos los libros favoritos del usuario """
    if 'user_id' not in session:
        return redirect('/')
    
    favorite_books = Libro.get_favorites_by_user({'user_id': session['user_id']})
    return render_template('favoritos.html', favorite_books=favorite_books)