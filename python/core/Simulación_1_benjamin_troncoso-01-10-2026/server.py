# Importamos la aplicación Flask configurada desde el paquete flask_app
from flask_app import app

# Importamos los controladores para registrar todas las rutas (endpoints) de la aplicación
from flask_app.controllers import usuarios
from flask_app.controllers import libros

# Verificamos si este archivo se está ejecutando directamente
if __name__ == "__main__":
    # Iniciamos el servidor local de desarrollo en el puerto 5000 con el modo depuración activo
    app.run(debug=True, port=5000)