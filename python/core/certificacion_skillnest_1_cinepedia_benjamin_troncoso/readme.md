# CinePedia 🎬

## Descripción del Proyecto
**CinePedia** es una aplicación web full-stack desarrollada con **Python**, **Flask** y una base de datos relacional **MySQL**. Su objetivo principal es permitir a los cinéfilos y usuarios registrarse, iniciar sesión de forma segura, compartir sus películas favoritas con detalles como director, fecha de estreno y sinopsis, además de interactuar comentando las publicaciones de otros miembros de la comunidad bajo un diseño moderno y responsivo basado en Bootstrap 5.

---

## Funciones Principales Utilizadas en el Proyecto

### 1. Sistema de Autenticación y Usuarios (`usuarios.py` / `Usuario`)
* **`index()`**: Muestra la página principal con las vistas combinadas de registro y inicio de sesión.
* **`registrar()`**: Valida los datos del formulario (nombre, apellido, formato de correo único y contraseña segura con mínimo 8 caracteres y confirmación), encripta la   contraseña usando **Flask-Bcrypt**, guarda al usuario en la base de datos y abre una sesión activa.
* **`login()`**: Verifica las credenciales ingresadas, comprueba que el email exista en la base de datos y valida el hash de la contraseña mediante `Bcrypt` para iniciar sesión.
* **`logout()`**: Limpia y destruye la sesión actual (`session.clear()`) redirigiendo al usuario a la página de inicio.

### 2. Gestión de Películas y CRUD (`cines.py` / `Pelicula`)
* **`dashboard()`**: Carga el panel principal protegido requiriendo sesión activa, listando todas las películas registradas en el sistema junto con su creador.
* **`nueva_pelicula()`**: Renderiza el formulario protegido para la creación de un nuevo registro cinematográfico.
* **`crear_pelicula()`**: Valida los campos (nombre único, director y sinopsis con longitud mínima requerida) y almacena la película relacionada al ID del usuario autenticado.
* **`ver_pelicula(id)`**: Muestra los detalles completos de una película en específico junto con todos sus comentarios asociados y el autor de cada uno mediante consultas `JOIN`.
* **`editar_pelicula(id)`**: Valida que el usuario logueado sea el propietario/creador original de la película antes de permitirle acceder al formulario de edición.
* **`actualizar_pelicula(id)`**: Procesa y valida las modificaciones hechas a los datos de la película y actualiza el registro en la base de datos.
* **`borrar_pelicula(id)`**: Valida la propiedad del registro y elimina la película de la base de datos de forma segura.

### 3. Sistema de Comentarios
* **`agregar_comentario(pelicula_id)`**: Permite a los usuarios enviar comentarios en las películas de la comunidad. Incluye una regla de validación de negocio (Bonus) que impide que un usuario comente su propia película.

### 4. Conexión y Seguridad (`mysqlconnection.py`)
* **`MySQLConnection` y `connectToMySQL`**: Clase y función auxiliar encargadas de gestionar la conexión con la base de datos MySQL mediante `PyMySQL` y variables de entorno seguras (`python-dotenv`), controlando automáticamente la ejecución de consultas y transacciones (`COMMIT`).

## Estructura de Archivos del Proyecto
```text
certificacion_skillnest_1_cinepedia_benjamin_troncoso/
│
├── .env                          
├── .gitignore                    
├── server.py                     
│
└── flask_app/                    
    ├── __init__.py               
    │
    ├── config/
    │   └── mysqlconnection.py    
    │
    ├── controllers/
    │   ├── categorias.py         
    │   ├── cines.py              
    │   └── usuarios.py          
    │
    ├── models/
    │   ├── categoria.py          
    │   ├── cine.py               
    │   └── usuario.py            
    │
    └── templates/
        ├── base.html           
        ├── dashboard.html        
        ├── editar_pelicula.html 
        ├── index.html            
        ├── nueva_pelicula.html   
        └── ver_pelicula.html     

---
**AUTOR**
benjamin troncoso 4°C