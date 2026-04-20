# hola_mundo.py (Versión SIN respuestas)


# 1. Imprime "Hola, mundo"
#    Reemplaza el comentario con el código necesario para que, al ejecutar,
#    aparezca en pantalla la frase "Hola, mundo".
#    Ejemplo de uso: print("Mensaje")
# ---------------------------------------------------------------
# (tu código aquí)

print("Hola mundo")


# 2. Imprime "Hola, Valeria" con el nombre en una variable
#    a) Concatenación usando comas
#    b) Concatenación usando +
# ---------------------------------------------------------------
bienvenida = "hola,"
nombre = " Valeria"

# a) Usando comas
# (tu código aquí)
print("hola," + (nombre))

# b) Usando +
# (tu código aquí)

print(bienvenida + nombre)


# 3. Imprime "Hola 156!" con el número en una variable
#    a) Usando comas
#    b) Usando + (esto podría dar error si no conviertes el número a str)
# ---------------------------------------------------------------
nose = "hola "
numero = 156

# a) Usando comas
# (tu código aquí)

print("hola " + str(numero))

# b) Usando +
# (tu código aquí)
# BONUS: Corrige el error con conversión de tipos si aparece.

print(nose + str(numero))


# 4. Imprime "Me encanta comer X e Y" con dos de tus comidas favoritas
#    a) Usando .format()
#    b) Usando f-strings
# ---------------------------------------------------------------
p = "pizza"
h = "hamburguesa"


# a) Con .format()
# (tu código aquí)

print("Me encanta comer {} e {}".format(p, h))

# b) Con f-string
# (tu código aquí)

print(f"Me encanta comer {p} e {h}")


# Desafío bonus: Usa al menos un método de cadena adicional.
# Ejemplo: .upper(), .lower(), .replace(), etc.
# ---------------------------------------------------------------
# (tu código aquí)

print("Me encanta comer {} e {}".format(p.lower(), h.upper()))

print(f"Me encanta comer {p.title()} e {h.replace('rolls', 'rollitos')}")