from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book

@app.route('/libros')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    
    all_books = Book.get_all()
    user_books = [b for b in all_books if b.user_id == session['user_id']]
    community_books = [b for b in all_books if b.user_id != session['user_id']]
    
    return render_template('dashboard.html', user_books=user_books, community_books=community_books)

@app.route('/libros/nuevo')
def new_book_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_book.html')

@app.route('/libros/crear', methods=['POST'])
def create_book():
    if 'user_id' not in session:
        return redirect('/')
    
    if not Book.validate_book(request.form):
        return redirect('/libros/nuevo')
    
    data = {
        "title": request.form['title'],
        "author": request.form['author'],
        "genre": request.form['genre'],
        "publication_date": request.form['publication_date'],
        "description": request.form['description'],
        "user_id": session['user_id']
    }
    Book.save(data)
    return redirect('/libros')

@app.route('/libros/<int:id>')
def show_book(id):
    if 'user_id' not in session:
        return redirect('/')
    
    book = Book.get_by_id({'id': id})
    users_favorited = Book.get_users_who_favorited({'book_id': id})
    user_already_favorited = any(u['id'] == session['user_id'] for u in users_favorited)
    
    return render_template('show_book.html', book=book, users_favorited=users_favorited, user_already_favorited=user_already_favorited)

@app.route('/libros/editar/<int:id>')
def edit_book_page(id):
    if 'user_id' not in session:
        return redirect('/')
    
    book = Book.get_by_id({'id': id})
    if book.user_id != session['user_id']:
        return redirect('/libros')
        
    return render_template('edit_book.html', book=book)

@app.route('/libros/actualizar/<int:id>', methods=['POST'])
def update_book(id):
    if 'user_id' not in session:
        return redirect('/')
    
    if not Book.validate_book(request.form):
        return redirect(f'/libros/editar/{id}')
        
    data = {
        "id": id,
        "title": request.form['title'],
        "author": request.form['author'],
        "genre": request.form['genre'],
        "publication_date": request.form['publication_date'],
        "description": request.form['description']
    }
    Book.update(data)
    return redirect('/libros')

@app.route('/libros/borrar/<int:id>')
def delete_book(id):
    if 'user_id' not in session:
        return redirect('/')
    
    book = Book.get_by_id({'id': id})
    if book and book.user_id == session['user_id']:
        Book.delete({'id': id})
    return redirect('/libros')

@app.route('/libros/favorito/<int:id>', methods=['POST'])
def add_favorite(id):
    if 'user_id' not in session:
        return redirect('/')
    
    Book.add_to_favorites({'user_id': session['user_id'], 'book_id': id})
    return redirect(f'/libros/{id}')

@app.route('/favoritos')
def favorites_page():
    if 'user_id' not in session:
        return redirect('/')
    
    favorite_books = Book.get_favorites_by_user({'user_id': session['user_id']})
    return render_template('favorites.html', favorite_books=favorite_books)