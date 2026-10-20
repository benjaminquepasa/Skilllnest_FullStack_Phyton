# Querido Diario 📖

## Descripción del Proyecto
**Querido Diario** es una aplicación web full-stack desarrollada con **Python**, **Flask**, **Jinja2** y una base de datos relacional **MySQL**. Su objetivo principal es permitir a los usuarios registrarse, iniciar sesión de forma segura y gestionar un diario personal digital donde pueden crear, editar, visualizar y eliminar sus propias entradas privadas con fechas y notas, además de incluir un sistema de búsqueda en tiempo real bajo un diseño moderno basado en Bootstrap 5 y variables de entorno protegidas con `python-dotenv`.

---

## Funciones Principales Utilizadas en el Proyecto

### 1. Sistema de Autenticación y Usuarios (`usuarios.py` / `Usuario`)
* **`index()`**: Muestra la página principal con las vistas combinadas de registro y inicio de sesión.
* **`registro()`**: Valida los datos del formulario (nombre, apellido, correo único, edad mínima de 18 años y contraseña segura de al menos 8 caracteres con confirmación), encripta la contraseña usando **Flask-Bcrypt**, guarda al usuario en la base de datos y abre una sesión activa.
* **`login()`**: Verifica las credenciales ingresadas, comprueba que el email exista en la base de datos y valida el hash de la contraseña mediante `Bcrypt` para iniciar sesión.
* **`logout()`**: Limpia y destruye la sesión actual (`session.clear()`) redirigiendo al usuario a la página de inicio.

### 2. Gestión de Entradas y CRUD (`entradas.py` / `Entrada`)
* **`dashboard()`**: Carga el panel principal protegido requiriendo sesión activa, listando todas las entradas de notas y fechas registradas por el usuario autenticado.
* **`nueva_entrada()`**: Renderiza el formulario protegido para la creación de un nuevo registro en el diario.
* **`crear_entrada()`**: Valida los campos (fecha no vacía, sin permitir fechas futuras como regla de negocio y notas obligatorias) y almacena la entrada relacionada al ID del usuario autenticado.
* **`ver_entrada(id)`**: Muestra los detalles completos de una entrada específica validando que pertenezca al usuario logueado.
* **`editar_entrada(id)`**: Valida que el usuario logueado sea el propietario original de la entrada antes de permitirle acceder al formulario de edición.
* **`actualizar_entrada(id)`**: Procesa y valida las modificaciones hechas a la fecha o notas y actualiza el registro en la base de datos.
* **`borrar_entrada(id)`**: Valida la propiedad estricta del registro para evitar alteraciones en la URL y elimina la entrada de forma segura.
* **`buscar(termino)`**: Permite filtrar y mostrar únicamente aquellas entradas del usuario que incluyan el término de búsqueda ingresado en las notas.

### 3. Conexión y Seguridad (`mysqlconnection.py`)
* **`MySQLConnection` y `connectToMySQL`**: Clase y función auxiliar encargadas de gestionar la conexión con la base de datos MySQL mediante **PyMySQL** y variables de entorno seguras (`python-dotenv`), controlando automáticamente la ejecución de consultas y transacciones (`COMMIT`).

---

## Estructura de Archivos del Proyecto
```text
certificacion_skillnest_intento_2_benjamin_troncoso/
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
    │   ├── entradas.py           
    │   └── usuarios.py           
    │
    ├── models/
    │   ├── entrada.py            
    │   └── usuario.py            
    │
    └── templates/
        ├── base.html             
        ├── buscar.html           
        ├── dashboard.html        
        ├── editar_entrada.html   
        ├── index.html            
        ├── nueva_entrada.html    
        └── ver_entrada.html

AUTOR:
Benjamin Toncoso