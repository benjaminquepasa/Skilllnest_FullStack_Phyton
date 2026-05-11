
"""➡️ Pasar argumentos 
Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al 
método __init__ y que de esta manera podamos asignarle a los atributos los valores 
correspondientes."""

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

#Creacion de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
bejmain = Usuario("benjamin", "troncoso", "benjamin@gmail.com", 10, 10)

#Imprimimos valores 
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#-----------------------------
#----Tarea rapida
"""
Crear una clase estudiante y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias par la clase con distintos estudiantes
- Imprimir el nombre y apellido concatenado + tu especialidad
"""
#Creacion de clase
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

#Creacion de instancias
benjamin = Estudiante(287463872, "bejamin", "troncoso", "programador", 5/3/2009)
isaias = Estudiante( 752237810, "isaias", "torres", "contabilidad", 6/10/2008)
linda = Estudiante( 228643728, "linda", "munoz", "logistica", 26/3/2009)

print(benjamin.nombre + " " + benjamin.apellido + " " + benjamin.especialidad) #Imprime: benjamin troncoso programador
print(isaias.nombre + " " + isaias.apellido + " " + isaias.especialidad) #Imprime: isaias torres contabilidad
print(linda.nombre + " " + linda.apellido + " " + linda.especialidad) #Imprime: linda munoz logistica