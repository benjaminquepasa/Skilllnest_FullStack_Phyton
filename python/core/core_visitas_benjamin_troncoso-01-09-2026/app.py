from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# La clave secreta es OBLIGATORIA para que Flask pueda encriptar las sesiones
app.secret_key = "clave_secreta_super_segura"


@app.route("/")
def index():
    # Nivel 1: Verificar e inicializar las visitas en la sesión
    if "visitas" not in session:
        session["visitas"] = 1
    else:
        session["visitas"] += 1

    # Nivel 3: Contador de cuántas veces se ha reiniciado el contador
    if "reinicios" not in session:
        session["reinicios"] = 0

    # Pasamos las variables del servidor al HTML
    return render_template(
        "index.html", visitas=session["visitas"], reinicios=session["reinicios"]
    )


@app.route("/sumar_dos")
def sumar_dos():
    # Nivel 2 / Bonus Plata: Incrementa en 2
    # OJO: Se suma 1 aquí porque al hacer redirect('/'), la ruta principal suma otro +1 (1 + 1 = 2)
    if "visitas" in session:
        session["visitas"] += 1
    return redirect("/")


@app.route("/sumar_custom", methods=["POST"])
def sumar_custom():
    # Nivel 3 / Bonus Oro: Formulario para sumar una cantidad específica
    cantidad = request.form.get("cantidad", type=int)
    if cantidad and "visitas" in session:
        # Se resta 1 para compensar el incremento de la ruta principal al redirigir
        session["visitas"] += cantidad - 1
    return redirect("/")


@app.route("/reiniciar")
def reiniciar():
    # Nivel 2 y 3: Reinicia el contador a 0 e incrementa las veces reiniciadas
    session["visitas"] = 0
    if "reinicios" in session:
        session["reinicios"] += 1
    else:
        session["reinicios"] = 1
    return redirect("/")


@app.route("/destruir_sesion")
def destruir_sesion():
    # Nivel 1: Borra absolutamente toda la sesión (limpia las cookies)
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)