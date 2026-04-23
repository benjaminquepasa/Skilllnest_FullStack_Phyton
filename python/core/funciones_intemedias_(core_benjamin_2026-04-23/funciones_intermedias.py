# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]

puntajes[1][0] = 600
print(puntajes)

# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]

streamers[0]["nombre"] = "EliteGamerX"

def imprimir_clave(clave, lista):
   for item in lista:
       print(item[clave])

imprimir_clave("nombre", streamers)
imprimir_clave("seguidores", streamers)

# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}

eventos["Estados Unidos"][2] = "San Francisco"

for categoria, lista in eventos.items():
   print(categoria)
   for item in lista:
       print(item)

# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

ubicacion[0]["latitud"] = "40.712776"
print(ubicacion)

#🎯 MINI DESAFÍO (nivel core)
datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]


# ejercicios numero 3   
categorias = {
   "4 juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "3 ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}

for categoria, lista in categorias.items():
   print(categoria)
   for item in lista:
       print(item)


#mostrar_informacion(categorias)

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(f"Nombre:{datos[2]["nombre"]} - {datos[2]["puntaje"]}")
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def cambiarPuntaje():
    print(f"{datos[0]["nombre"]} obtuvo {datos[0]["puntaje"]} puntos")
cambiarPuntaje()
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def imprimirDatos(nombre):
    if nombre == "Maria":
        print(f"nombre:{datos[1]["nombre"]} - {datos[1]["puntaje"]}")