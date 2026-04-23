#Funciones en python
def multiplicacion(num1, num2): #Definimos la funcion mutliplicacion con los parametros num1, num2
    resultado = num1 * num2  #Instrucciones dentro de la funcion
    return resultado  #Regresamos valor de resultado

a = int(input("Ingrese pimer numero:"))
b = int(input("Ingrese segundo numero:"))
resultado_multiplicacion = multiplicacion(a, b)
print(resultado_multiplicacion)


#Parametros y argumentos
def buenos_dias(nombre):
    print("buenos dias " + nombre)
    

#Una ves definida la funcion, podemos invocarla llamandola por su nombre y enviando la cantidad de argumentos requerido:
buenos_dias("alegria")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor sol")

#Devolucion de valores
def buenoos_dias2(nombre):
    return "buenos dias " + nombre

#El valor de retorno de la funcion es "Buneos dias python", por lo que el valor de el variable frase sera que

frase =  buenoos_dias2("python")
print(frase) #Imprime: Buenos dias python

#Ejerecicio de retorno de valor
#Crear una funcion que reciba dos parametros (una frase y una palabra)
#Devolver el valor de la frase completa e imprimir

def construirFrase(frase, palabra):
    return f"{frase} {palabra}"

frase = input("Ingrese una frase:")
palabra = input("Ingrese una palabra:")
resultadoFrase = construirFrase(frase, palabra)
print(resultadoFrase)