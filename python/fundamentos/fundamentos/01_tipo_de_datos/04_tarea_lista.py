"""
Actividad gestor de inventario
"""

""" 1.- Creacion: Crear una lista llamada inventario que contenga los siguientes
articulos: "laptop", "raton", "monitor", "cable hdmi"."""

articulos = ["laptop", "raton", "monitor", "cable hdmi"]
print(articulos)

""" 2.-Expansion: Utiliza el metodo correspondiente para agregar "impresora" y "teclado"
al final de la lista"""


articulos.append("impresora")
articulos.append("teclado")
print("Lista con 2 elementos agregados:",articulos)

""" 3.-Conteo: Utiliza la funcion integrada para mostrar cuanto elementos
totales hay en la lista. """

print(len(articulos))

""" 4.-Acceso y  modificacion: Modifica "teclado" por "teclado mecanico" """

articulos[5] = "teclado mecanico"

""" 5.-Slicing: Crea una nueva lista llamda "promocion", debe contener
solo los 3 primeros elemntos de la lista "inventario". """

promocion = ["teclado", "raton", "laptop"]

""" 6.-Mostrar la lista de inventario ordenado alfabeticamente."""

articulos.sort()
print(articulos)

""" 7.-Elimina el ultimo elemento de la lista inventario mostrando el elemento
eliminado y la lista final"""

eliminado = articulos.pop()

print("Elemento eliminado:", eliminado)
print("lista final", articulos)