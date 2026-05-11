

class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0
       
   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
       
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra de {miyagi.nombre}: ${segundacompra}")
#Imprimir cuanto credito le queda a miyagi
print(f"Credito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")
print("-------Compras de daniel-------")
daniel.hacer_compra(45)
print(daniel.saldo_pagar) # Imprime 45

#Tarea 
"""1.-Crea un nuevo metodo que permita aumentar el limite de credito.
Imprimir el nuevo limite de credito"""
miyagi.limite_credito += 10000
print(f"El nuevo limite de credito es: {miyagi.limite_credito}")

"""2.-Crear un metodo que permita cambiar el correo de la instancia.
Mostar el nuevo correo"""
miyagi.cambiarCorreo("Miyagisacamela@gmail.com")
print(f"El nuevo cooreo establecido es: {miyagi.email}")