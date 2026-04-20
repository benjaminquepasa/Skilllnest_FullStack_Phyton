#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.

def numerosDinamicos():
    
  numero = int(input("Ingresa cuantos numeros pares quieres mostrar:"))
  contador = 1

  while contador <= numero:
    print(contador * 2)
    contador += 1


#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.

def verificadorEdad():
  edad = int(input("Ingrese su edad:"))

  if edad <= 18:
    falta = 18 - edad
    print("no eres mayor de edad te faltan", falta, "años")
  elif edad > 18:
    print("Eres mayor de edad")
    

#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.

def calculadoraDescuento():
  precio = int(input("Ingresa el precio del producto:"))
  cantidad = int(input("Ingresa la cantidad del producto:"))

  subtotal = precio * cantidad

  descuento = 0

  if subtotal > 100:
    descuento = subtotal * 0.15
    
  total = subtotal - descuento

  print("Subtotal: ", subtotal)
  print("Descuento: ", descuento)
  print("Total a pagar: ", total)

#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.

def clasificarNumeros():
# Pedir número al usuario
  numero = int(input("Ingrese un número: "))

# Evaluar el número
  if numero == 0:
    print("Cero")
  elif numero > 0:
    if numero % 2 == 0:
        print("Positivo-Par")
    else:
        print("Positivo-Impar")
  else:
    if numero % 2 == 0:
        print("Negativo-Par")
    else:
        print("Negativo-Impar")

#II. Iteraciones y Bucles (Intermedio)
#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.

# Solicitar número al usuario
numero = int(input("Ingrese un número entero: "))

# Generar la tabla del 1 al 12
for i in range(1, 13):
    resultado = numero * i
    
    # Mostrar solo si es múltiplo de 3
    if resultado % 3 == 0:
        print(f"{numero} x {i} = {resultado}")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).

# Inicializar la suma
suma = 0

while True:
    numero = int(input("Ingrese un número (negativo para terminar): "))
    
    if numero < 0:
        break  # Termina el ciclo si es negativo
    
    suma += numero  # Acumula la suma

# Mostrar resultado final
print("La suma total es:", suma)

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.

# Pedir texto al usuario
texto = input("Ingrese una frase o palabra: ")

# Inicializar contador
contador = 0

# Recorrer cada carácter
for letra in texto:
    if letra.lower() in "a,e,i,o,u":
        contador += 1

# Mostrar resultado
print("Cantidad de vocales:", contador)

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.

# Definir la contraseña
contrasena = "Programacion"

# Número máximo de intentos
intentos_max = 3

for intento in range(1, intentos_max + 1):
    ingreso = input("Ingrese la contraseña: ")
    
    if ingreso == contrasena:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta")
        
        if intento == intentos_max:
            print("Acceso bloqueado")

#III. Manejo de Arreglos / Listas (Avanzado)
#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.

# Crear lista vacía
nombres = []

# Pedir 5 nombres
for i in range(5):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)

# Mostrar en orden inverso
print("Nombres en orden inverso:")
for nombre in reversed(nombres):
    print(nombre)

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.

# Solicitar cantidad de notas
cantidad = int(input("¿Cuántas notas desea ingresar? "))

# Crear lista para almacenar notas
notas = []

# Ingresar las notas
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

# Calcular resultados
promedio = sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)

# Mostrar resultados
print("Promedio:", promedio)
print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.

# Solicitar cantidad de números
cantidad = int(input("¿Cuántos números desea ingresar? "))

# Crear lista original
numeros = []

# Ingresar los números
for i in range(cantidad):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Crear nuevo arreglo con números mayores a 50
mayores_50 = [n for n in numeros if n > 50]

# Mostrar resultados
print("Arreglo original:", numeros)
print("Números mayores a 50:", mayores_50)

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.

# Lista de 10 ciudades
ciudades = ["Madrid", "París", "Londres", "Roma", "Berlín", 
            "Lisboa", "santiago", "Viena", "Praga", "valparaiso"]

# Pedir ciudad al usuario
busqueda = input("Ingrese el nombre de una ciudad: ")

# Verificar si la ciudad está en la lista
if busqueda in ciudades:
    indice = ciudades.index(busqueda)
    print(f"La ciudad '{busqueda}' se encuentra en la lista en la posición {indice}.")
else:
    print(f"La ciudad '{busqueda}' NO se encuentra en la lista.")
    
#IV. Retos de Lógica Combinada
#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].

# Crear listas vacías
nombres_productos = []
precios = []

# Pedir 3 productos y sus precios
for i in range(3):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: $"))
    
    nombres_productos.append(nombre)
    precios.append(precio)

# Mostrar inventario formateado
print("\nInventario:")
for i in range(3):
    print(f"Producto: {nombres_productos[i]} - Precio: ${precios[i]:.2f}")

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.

# Crear lista vacía de compras
lista_compras = []

# Pedir artículos al usuario
while True:
    articulo = input("Ingrese un artículo (o 'terminar' para finalizar): ")
    if articulo.lower() == "terminar":
        break
    lista_compras.append(articulo)

# Ordenar la lista alfabéticamente
lista_compras.sort()

# Mostrar lista final
print("\nLista de compras ordenada:")
for item in lista_compras:
    print(item)
    
#15. Análisis de Temperaturas
    #Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:

# Lista para guardar temperaturas
temperaturas = []

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Solicitar temperaturas
for dia in dias:
    temp = float(input(f"Ingrese la temperatura de {dia}: "))
    temperaturas.append(temp)

# Mostrar temperaturas ingresadas
print("\nTemperaturas de la semana:", temperaturas)

# Calcular estadísticas
temp_max = max(temperaturas)
temp_min = min(temperaturas)
promedio = sum(temperaturas) / len(temperaturas)

# Mostrar resultados
print("Temperatura más alta:", temp_max)
print("Temperatura más baja:", temp_min)
print("Promedio de la semana:", promedio)

continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("---1.-Ejercicio---")
    print("---2.-Ejercicio---")
    print("---3.-Ejercicio---")
    print("---4.-Ejercicio---")
    print("---5.-Ejercicio---")
    print("---6.-Ejercicio---")
    print("---7.-Ejercicio---")
    print("---8.-Ejercicio---")
    print("---9.-Ejercicio---")
    print("---10.-Ejercicio---")
    print("---11.-Ejercicio---")
    print("---12.-Ejercicio---")
    print("---13.-Ejercicio---")
    print("---14.-Ejercicio---")
    print("---15.-Ejercicio---")
    
    opcion = input("\n----Elige una opcion: (1-15) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercico 1:")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nEjecutando ejercico 2:")
        print(verificadorEdad)
    elif opcion == "3":
        print("\nEjecutando ejercico 3:")
        print(calculadoraDescuento())
    elif opcion == "4":
        print("\nEjecutando ejercico 4:")
        print(clasificarNumeros())