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

message = "My first bicycle was a " + bycicles[0].title() + "."
print(message)

message_final = f"My last bicycle was a {bycicles[-1].title()}."
print(message_final)

##Agregar elementos a una lista
motorcycles = ["honda,", "yamaha", "suzuki"]
print("Lista original de motocicletas: ", motorcycles)

motorcycles.append("ducati")  # Agrega un elemento al final de la lista
print("Lista después de agregar un elemento: ", motorcycles)

"""

    El método append() agrega un elemento al final de la lista.

"""
# Crear una lista vacía y agregar elementos
cars = []
print("Lista de carros: ", cars)
cars.append("bmw")
print("Lista de carros: ", cars)
cars.append("audi")
print("Lista de carros: ", cars)
cars.append("toyota")
print("Lista de carros: ", cars)

# Agregar un elemento en una posición específica
motorcicles = ["honda", "yamaha", "suzuki"]
print("Lista original de motocicletas: ", motorcicles)
motorcicles.insert(1, "ducati")  # Agrega un elemento en la posición 0
print("Lista después de insertar un elemento: ", motorcicles)

print("--------------------------------")
# Eliminar elementos de una lista usando del
print("Lista original de motocicletas: ", motorcicles)
del motorcicles[0]  # Elimina el elemento en la posición 2
print("Lista después de eliminar un elemento: ", motorcicles)

print("---------------POP-----------------")
# Eliminar un elemento usando el método pop()
print("Lista original de motocicletas: ", motorcicles)
popped_motorcycle = motorcicles.pop()  # Elimina el último elemento de la lista y lo asigna a una variable
print("Lista después de hacer pop(): ", motorcicles)
print("Motocicleta sacada con pop(): ", popped_motorcycle)

print("---------------POP(ÍNDICE)-----------------")
# Eliminar un elemento en una posición específica usando pop()
first_motoricicle = motorcicles.pop(0)  # Elimina el primer elemento de la lista y lo asigna a una variable
print("Lista después de hacer pop(0): ", motorcicles)
print("Primera motocicleta sacada con pop(0): ", first_motoricicle)

