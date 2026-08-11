from flask import Flask, render_template, request

app = Flask(__name__)

# Lista simple con los datos de las 8 frutas
FRUTAS = {
    'manzana': {'nombre': 'Manzana', 'precio': 2.5, 'imagen': 'manzana.png', 'desc': 'Fruta dulce y crujiente, rica en fibra.'},
    'platano': {'nombre': 'Plátano', 'precio': 1.8, 'imagen': 'platano.png', 'desc': 'Fruta energética rica en potasio.'},
    'naranja': {'nombre': 'Naranja', 'precio': 3.0, 'imagen': 'naranja.png', 'desc': 'Cítrico jugoso rico en vitamina C.'},
    'fresa': {'nombre': 'Fresa', 'precio': 4.5, 'imagen': 'fresa.png', 'desc': 'Baya dulce y aromática.'},
    'uva': {'nombre': 'Uva', 'precio': 3.8, 'imagen': 'uva.png', 'desc': 'Fruta pequeña y dulce.'},
    'pina': {'nombre': 'Piña', 'precio': 5.0, 'imagen': 'pina.png', 'desc': 'Fruta tropical dulce y ácida.'},
    'sandia': {'nombre': 'Sandía', 'precio': 4.2, 'imagen': 'sandia.png', 'desc': 'Fruta refrescante para el verano.'},
    'mango': {'nombre': 'Mango', 'precio': 3.5, 'imagen': 'mango.png', 'desc': 'Fruta tropical muy dulce.'}
}

# Ruta 1: Inicio (Formulario para comprar)
@app.route('/')
def index():
    return render_template("index.html", frutas=FRUTAS)

# Ruta 2: Catálogo simple
@app.route('/frutas')
def frutas():
    return render_template("frutas.html", frutas=FRUTAS)

# Ruta 3: Resumen del pedido
@app.route('/checkout', methods=['POST'])
def checkout():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    direccion = request.form.get('direccion')

    compras = []
    total_frutas = 0
    total_dinero = 0.0

    # Recorremos cada fruta para ver cuántas pidió el usuario
    for clave, info in FRUTAS.items():
        cantidad = int(request.form.get(clave, 0))
        if cantidad > 0:
            # Redondeamos el subtotal a 2 decimales para evitar decimales infinitos
            subtotal = round(cantidad * info['precio'], 2)
            total_frutas += cantidad
            total_dinero += subtotal
            compras.append({
                'nombre': info['nombre'],
                'precio': info['precio'],
                'cantidad': cantidad,
                'subtotal': subtotal,
                'imagen': info['imagen']
            })

    return render_template(
        "checkout.html",
        nombre=nombre,
        email=email,
        direccion=direccion,
        compras=compras,
        total_frutas=total_frutas,
        total_dinero=round(total_dinero, 2)  # Redondeamos el total a 2 decimales
    )

if __name__ == "__main__":
    app.run(debug=True)