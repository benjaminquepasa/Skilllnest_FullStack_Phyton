"""
🗂️ Define la clase UsuarioStreaming, que debe incluir:

Atributos:
nombre
email
suscripcion (Gratis, Estándar o Premium)
lista_reproduccion (lista de títulos agregados por el usuario).
Métodos:
agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
"""

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

benjamin = UsuarioStreaming("Benjamin", "benjamin@gmail.com", "Premium")
juan = UsuarioStreaming("Juan", "juan@gmail.com", "Gratis")
elisa = UsuarioStreaming("Elisa", "elisa@gmail.com", "Estandar")

def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(f"titulo {titulo} Agregado correctamente")
        
def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        print(titulo)
        
def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        self.susubscripcion = input("Intrudice el nuevo tipo de suscripción:")
        
def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        print(f"Nombre: {benjamin.nombre}")
        print(f"Email: {benjamin.email}")
        print(f"Suscripción: {benjamin.suscripcion}")
        print(f"Lista de reproducción: {benjamin.lista_reproduccion}")
        
        print(f"Nombre: {juan.nombre}")
        print(f"Email: {juan.email}")
        print(f"Suscripción: {juan.suscripcion}")
        print(f"Lista de reproducción: {juan.lista_reproduccion}")
        
        print(f"Nombre: {elisa.nombre}")
        print(f"Email: {elisa.email}")
        print(f"Suscripción: {elisa.suscripcion}")
        print(f"Lista de reproducción: {elisa.lista_reproduccion}")