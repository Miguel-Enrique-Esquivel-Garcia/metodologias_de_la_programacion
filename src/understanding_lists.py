# LISTAS
"""
    Las listas nos permiten almacenar información en un lugar,
    'la cantidad que tengas' : ya sean pococ elementos o millones de elementos.


    Se recomienda nombrar una variable del tipo lista en PLURAL.

    En Python los corchetes [] indican o definen una lista,
    los elementos dentro de la lista van separados por comas.

    Ejemplo:
"""
# Definición de una lista
bycicles = ['trek', 'cannondale', 'redline', 'giant']
print(bycicles, type(bycicles))

# acceder a un elemento de la lista
print(bycicles[0].title(), type(bycicles[0]))  # Primer elemento de la lista
print(bycicles[1].title(), type(bycicles[1]))  # Segundo elemento de la lista
print(bycicles[2].title(), type(bycicles[2]))  # Tercer elemento de la lista
print(bycicles[3].title(), type(bycicles[3]))  # Cuarto elemento de la lista

# Acceder al último elemento de la lista
print(bycicles[-1].title(), type(bycicles[-1]))  # Último elemento de la lista
print(bycicles[-2].title(), type(bycicles[-2]))  # Penúltimo elemento de la lista
print(bycicles[-3].title(), type(bycicles[-3]))  # Antepenúltimo elemento de la lista
print(bycicles[-4].title(), type(bycicles[-4]))  # Cuarto elemento de la lista