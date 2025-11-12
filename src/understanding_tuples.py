"""
    Tuplas: Las tuplas son listas de elementos que no cambian de tamaño.
    Las tuplas son listas inmutables.

    Se utilizan los () para definir una tupla.
    O la palabra reservada tuple().

    Si tenemos un rectángulo que siempre va a tener cierto tamaño, podemos asegurar que su tamaño no va a cambiar
    si colocamos sus valores en una tupla.
"""

# Ejemplo de tuplas
dimensions = (200,50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# dimensions[0]=300 #NOSEPUEDE

for dimension in dimensions:
    print(dimension)

"""
    No podemos modificar una tupla directamente
    lo que si podemos hacer es cambiar la asignación
    a una variable que almacena una tupla.
"""
dimensions = (200,50)
print(dimensions)
dimensions = (400, 100, 25)
print(dimensions)