class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

   def __init__(self, usuario, tipo_suscripcion="Gratis"):
       self.usuario = usuario
       self.salfo_pendiente = self.salfo_pendiente
       self.tipo_suscripcion = tipo_suscripcion
       self.costo_suscripcion = self.costos_suscripcion[tipo_suscripcion]
       

   def realizar_pago(self, monto):
       """Reduce el saldo pendiente según el monto pagado."""
       self.saldo_pendiente -= monto
       if self.saldo_pendiente < 0:
           self.saldo_pendiente = 0

   def cambiar_suscripcion(self, nuevo_tipo):
       """Cambia el tipo de suscripción y actualiza el costo mensual."""
       self.tipo_suscripcion = nuevo_tipo
       self.costo_suscripcion = self.costos_suscripcion[self.tipo_suscripcion]

   def ver_contenido_exclusivo(self):
       """Permite ver contenido exclusivo según el tipo de suscripción."""
       if self.tipo_suscripcion == "Gratis":
           return "Contenido Gratis"
       elif self.tipo_suscripcion == "Estándar":
           return "Contenido Estándar"
       elif self.tipo_suscripcion == "Premium":
           return "Contenido Premium"
       else:
           return "Contenido Gratis"

   def mostrar_info_suscripcion(self):
       """Muestra la información de la suscripción del usuario."""
       print(f"Suscripción de {self.usuario.nombre}")
       print(f"Tipo de suscripción: {self.tipo_suscripcion}")    
       print(f"Costo mensual: {self.costo_suscripcion}")
   
benjamin = SuscripcionStreaming("estandar")
alexander = SuscripcionStreaming("premium")
randy = SuscripcionStreaming("gratis")