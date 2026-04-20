# Condicionales
# Estructura else - if

num = 15
if num > 20:
   print("Número mayor a 20")
else:
   print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''
num = 101
if num > 50:
   print("Número mayor a 50")
elif num > 100:
   print("Número mayor a 100")
else:
   print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
   print("Número menor a 50")

#No se cumple con la condicional, por lo que no se ejecuta el bloque de código

# Tarea desafio
#Ingresa 3 numeros por teclados e identificar cual es el mayor y cual es el menor mostar ambos

num1 = int(input("Ingresar primer numero:"))
num2 = int(input("Ingresa el segundo numero:"))
num3 = int(input("Ingresa el tercer numero:"))

# Estructura if - elfi - else
if num1 >= num2 and num1 >= num3:
   mayor = num1
   if num2 <= num3:
      menor = num2
   else:
      menor = num3
elif num2 >= num1 and num2 >= num3:
   mayor = num2
   if num1 <= num3:
      menor = num1
   else:
      menor = num3
else:
   mayor = num3
   if num1 <= num2:
      menor  = num1
   else:
      menor = num2
print(f"El mayor es {mayor} y el menor es {menor}")