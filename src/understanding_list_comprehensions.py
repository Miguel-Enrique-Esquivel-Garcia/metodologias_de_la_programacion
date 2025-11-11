"""
    Un list comprehension combina el for loop y la creación de nuevos elementos en una sola línea
    y automátiicamente agrega cada nuevo elemento a la lista, sin tener que usar el método append().
"""
# Generar una lista con los cuadrados de los primeros 10 números usando list comprehension
squared = [number ** 2 for number in range(1, 11)]
print(squared)

# Generar una lista con los números pares
evens = [number for number in range(101) if number % 2 == 0]
print(evens)

# Generar una lista con los números impares
odds = [number for number in range(101) if number % 2 != 0]
print(odds)