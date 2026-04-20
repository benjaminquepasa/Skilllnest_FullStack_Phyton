"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # Importación de libreria para porcesos aleatorios


nombre = "Frida Kahlo" # Creacion de variable tipo String(texto) y se asigna valor
print(type(nombre)) # type() = metodo de python para mostar el tipo de una variable
print(len(nombre)) # len() = Devuelve el largoo de una variable


edad = 25 # Creacion de una variable tipo numerico(int)


if edad < 18: # Se estable condicion if.
   print("Eres menor de edad.") # Imprime un mensaje
elif edad == 18: # se estable subcondicipn tipo elif(else if)
   print("Tienes 18 años.") # Imprime un mensaje
else: # Cierre de condicion(si no se cumplen codiciones anteriores)
   print("Eres mayor de edad.") #I mprime un mensaje


frutas = ["manzana", "pera", "fresa"] # Creamos un arreglo(array) con valores ya asignados
print(frutas[0]) # Mostramos la primera posicion del arreglo
frutas[0] = "banana" # A la posicion 0 del arrgelo se le asigna el valor "banana"
frutas.append("uva") # Se le agrega "uva" al final del arreglo
frutas.remove("pera") # Se remueve la palabra "pera" del arreglo


dimensiones = (200, 50) # Creamos una variable tipo tupla(variable inmmutable)
print(dimensiones[0]) # Imprime la posicion 0 de la variable creada


persona = {  # Variable tipo object (objeto)
   "nombre": "Carlos", # Se establece un item y su respectivo valor
   "edad": 30 # Se establece un item y su respectivo valor
}
print(persona["nombre"]) # Imprime el valor del item(ej: "carlos")
persona["edad"] = 31 # Se modifica el valor del item edad 31
persona["ciudad"] = "Santiago" # Se agrega un nuevo item con un valor
del persona["ciudad"] # Se elimina el item completo


for i in range(5): # for range:Se crea bucle de rango desde 0 a 5
   if i == 2: # Se establece codicion if i == 2
       continue # Continue ignora el proceso y continua
   if i == 4:# Se establece codicion if i == 4
       break # Si i = 4 se rompe el bucle
   print(i) # Imprime el valor de i en cada interaccion.(hasta 4)


contador = 0 # Se crea una variable contador valor numerica(int)
while contador < 3: # Se crea blucle while con una conidición
   print(f"while contador es: {contador}") # Imprime el contador en un mensaje concatenado con f"" string
   contador += 1 # Incrementa el valor en 1 en cada interaccion


def saludar_usuario(nombre): # def - palabra reservada para crear una funcion
   return f"Hola, {nombre}" # Devuelve un valor de la funcion


print(saludar_usuario("Francisca")) # Se imprime "Hola Francisca" - return de la funcion