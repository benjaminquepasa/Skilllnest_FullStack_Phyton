#Creacion de la clase usuarios - entidad
class Usuario:
  def __init__(self): # Contructor de la clase| self: Crear las variables de una clase(referencia)
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0 #Pronto pondremos métodos y atributos

# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
benjamin = Usuario()

print(benjamin.nombre) #Imprime: Benjamin

#Valores a nuevas instancias
benjamin.nombre = "Benjamin"
benjamin.apellido = "Larusso"
benjamin.email = "benjamin@gmail.com"
benjamin.limite_credito = 10  
benjamin.saldo_pagar = 1000000

#Accedemos a los atributos de la instancia
print(miyagi.nombre) # imprime "Nariyoshi"
print(miyagi.apellido) # imprime "Miyagi"
print(miyagi.email) # imprime "miyagi@codingdojo.la"
print(miyagi.limite_credito) # imprime 30000
print(miyagi.saldo_pagar) # imprime 0

# Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "danielarusso@codingdojo.la"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido) #Imprime: Larusso
print(daniel.email) #Imprime: danielarusso@codingdojo.la
print(daniel.limite_credito) #Imprime: 100000    
print(daniel.saldo_pagar) #Imprime: 300000

#Imprimir nombres de cada instancia
print(benjamin.nombre) #Imprime: Benjamin
print(daniel.nombre) #Imprime: Daniel
print(miyagi.nombre) #Imprime: Nariyoshi