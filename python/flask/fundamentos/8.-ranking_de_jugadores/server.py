from flask import Flask, render_template

app = Flask(__name__)

# Datos de jugadores con puntajes, niveles y países
jugadores = [
    {"nombre": "AlexGamer", "puntaje": 5000, "nivel": 42, "pais": "Chile"},
    {"nombre": "PixelMaster", "puntaje": 7500, "nivel": 58, "pais": "Argentina"},
    {"nombre": "ShadowNinja", "puntaje": 8200, "nivel": 61, "pais": "México"},
    {"nombre": "CyberWarrior", "puntaje": 9100, "nivel": 75, "pais": "Colombia"},
    {"nombre": "UltraNoob", "puntaje": 3000, "nivel": 12, "pais": "España"}
]

# 1. Ruta base oficial del desafío
@app.route("/ranking")
def ranking():
    jugadores_ordenados = sorted(jugadores, key=lambda x: x['puntaje'], reverse=True)
    return render_template(
        "ranking.html",
        jugadores=jugadores_ordenados,
        color=None
    )

# 2. Ruta para limitar la cantidad de jugadores visibles
@app.route("/ranking/<int:cantidad>")
def ranking_limitado(cantidad):
    jugadores_ordenados = sorted(jugadores, key=lambda x: x['puntaje'], reverse=True)
    return render_template(
        "ranking.html",
        jugadores=jugadores_ordenados[:cantidad],
        color=None
    )

# 3. Ruta para limitar la cantidad de jugadores Y cambiar el color de fondo
@app.route("/ranking/<int:cantidad>/<color>")
def ranking_color(cantidad, color):
    jugadores_ordenados = sorted(jugadores, key=lambda x: x['puntaje'], reverse=True)
    return render_template(
        "ranking.html",
        jugadores=jugadores_ordenados[:cantidad],
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)