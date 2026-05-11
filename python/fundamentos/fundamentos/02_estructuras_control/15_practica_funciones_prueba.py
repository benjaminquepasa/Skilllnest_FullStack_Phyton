import os
"""
Instrucciones generales
Deberá desarrollar un programa en Python que contenga un menú interactivo utilizando la estructura while, permitiendo al usuario seleccionar distintas opciones para ejecutar funciones previamente definidas.
Cada opción del menú deberá llamar a una función diferente, la cual resolverá una situación específica utilizando distintos tipos de datos como enteros, decimales, cadenas de texto, listas y diccionarios.
En aquellos casos donde sea necesario, deberá solicitar información al usuario mediante input(). Además, se deberá trabajar con arreglos (listas) para recorrer información utilizando ciclos for, junto con estructuras condicionales como if, elif y else.
El programa deberá incluir una opción para salir correctamente del sistema.

Ejercicios a desarrollar
Su programa deberá considerar las siguientes funciones:
1.-Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
3.-Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
4.-Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
5.-Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
6.-Crear una función que reciba un número entero y determine si es par o impar.
7.-Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
8.-Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
9.-Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
10.-Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.

Requisitos obligatorios
Su trabajo debe cumplir con lo siguiente:
Uso de funciones con parámetros
Uso de menú con ciclo while
Uso de input() para solicitar datos
Uso de listas (arreglos)
Uso de diccionarios
Uso de ciclos for
Uso de estructuras condicionales (if, elif, else)
Código ordenado, comentado y correctamente indentado
Opción de salida del programa (0. Salir)
"""
# Ejerecicio numero 1
def numeroMayor(listado):
    menor = menor(listado)
    mayor = mayor(listado)
    print(f"El mayor es {mayor} y el menor es {menor}")

def ejercicio1():
    limit = int(input("ingresa un limite de valores:"))
    listadoNum = []
    i = 1
    while i <= limit:
        num = int(input(f"Ingresa un numero entero {i} de {limit}:"))
        listadoNum.append(num)
        i += 1
    numeroMayor(listadoNum)

# Ejerecicio numero 2
def cadena(cadena):
    cadena = input("Ingresa una cadena de texto:")
    numero = 0
    for letra in cadena:
      if letra.lower() in "a,e,i,o,u,A,,E,I,O,U":
        numero += 1
    print(f"cantidad de vocales son: {numero}")

# Ejerecicio numero 3
# Ejerecicio numero 2
def filtar(lista):
    resulatdo = []
    for nombre in lista:
        if len(nombre) > 5:
            resulatdo.append(nombre)
    return resulatdo

def mostar():
    nombres = []
    cantidad = int(input("¿Cuantos nombres quieres ingresar?"))

    for i in range(cantidad):
        nombre = input("Ingresa un nombre: ")
        print(f"{nombre} agregado con exito a la lista")
        nombres.append(nombre)
        
    listaNombres = filtar(nombres)
    print(f"Los nombres con más de 5 letras son: {listaNombres}")

# Ejerecicio 4
def listaNotas(notas):
    lista = 0
    for i in range(len(notas)):
        lista += notas[i]
        if notas[i] > 4.0 and notas[i] <= 7.0:
            print(f"El estudainte {i + 1} pasa con un {notas[i]}")
        elif notas[i] < 4.0 and notas[i] >= 1.0:
            print(f"El estudanite {i + 1} no pasa con un {notas[i]}")
        else:
            print("error")
        return lista / (len(lista) + 1)
    
def ejericio4():
    largo = int(input("¿Cuantas notas vas a ingresar?"))
    nota = []
    for i in range(largo):
        inp = float(input(f"ingresa una nota {i + 1}"))
        if inp != "":
            nota.append(inp)
    print(listaNotas(nota))

# E ejercicio 5
def descuento(valor) :
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * (90 / 100)
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es: \n{precioInicial}\ny con descuento \n{precioFinal}")
    
def valores():
    cantidadProducto = int(input("Ingresa la cantidad de productos que quiera: \n"))
    listaPrecio = []
    for i in range(cantidadProducto):
        valorProducto = float(input("Ingrese el valor del producto: \n"))
        listaPrecio.append(valorProducto)
    descuento(listaPrecio)
    
# Ejercicio 6
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    elif numero % 3 == 0:
        print(f"El numero {numero} es impar")
    else:
        print("error")
        
def recibirNumero():
    num = int(input("Ingresa un numero: "))
    parImpar(num)


def limpiar_consola():
    os.system('cls')

continuar = True
while continuar:
    print("\n --Ejerecicios python---")
    print("---1.- Ejercicio 1 ---")
    print("---2.- Ejercicio 2 ---")
    print("---3.- Ejercicio 3 ---")
    print("---4.- Ejercicio 4 ---")
    print("---5.- Ejercicio 5 ---")
    print("---6.- Ejercicio 6 ---")
    
    opcion = input("\n----Elige una opcion: (1 - 6) (0 para salir) =")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1: ")
        print(ejercicio1())
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutando ejercicio 2: ")
        print(cadena(cadena))
    elif opcion == "3":
        limpiar_consola()
        print("\nEjecutando ejercicio 3: ")
        print(mostar())
    elif opcion == "4":
        limpiar_consola()
        print("\nEjecutando ejercicio 4: ")
        print(ejericio4())
    elif opcion == "5":
        limpiar_consola()
        print("\nEjecutando ejercicio 5: ")
        print(valores())
    elif opcion == "6":
        limpiar_consola()
        print("\nEjecutando ejercicio 6: ")
        print(recibirNumero())
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        limpiar_consola()
        print("Opcion no valida, intenta otra vez")