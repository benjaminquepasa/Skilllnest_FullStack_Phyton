from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Lista de diccionarios con la información de la imagen
    plataformas = [
        {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia"},
        {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
        {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
        {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
        {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
        {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
        {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]
    
    # Pasamos la lista a la plantilla index.html
    return render_template('index.html', datos=plataformas)

if __name__ == '__main__':
    app.run(debug=True)