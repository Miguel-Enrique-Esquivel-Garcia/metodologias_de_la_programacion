"""
Las listas también pueden almacenar números y de hecho son ideales para eso.
Python ofrece muchas herramientas que ayudan a trabajar de manera eficiente las listas de números.
"""

# Método range()
# Nos ayuda a generar fácilmente series de números
# Ejemplo:
print("Imprime los primeros 10 números (0-9)")
for number in range(10):
    print(number)
first_10_numbers = list(range(10))
print(first_10_numbers)

print("Imprime los números del 1 al 4")
for number in range(1,5):
    print(number)
numbers_1_to_4 = list(range(1,5))
print(numbers_1_to_4)

print("Imprime los números pares del 0 al 10")
for number in range(0,11,2):
    print(number)
even_numbers_0_to_10 = list(range(0,11,2))
print(even_numbers_0_to_10)

print("Imprime los números impares del 1 al 10")
for number in range(1,11,2):
    print(number)
odd_numbers_1_to_10 = list(range(1,11,2))
print(odd_numbers_1_to_10)

print("Imprime la tabla del 5")
for number in range(0,51,5):
    print(number)
multiples_of_5 = list(range(0,51,5))
print(multiples_of_5)

print("Generar una lista con los cuabrados \
de los primeros 10 números")
squared = []
for number in range(1,11):
    square = number ** 2
    squared.append(square)
print(squared)

##### Otro métodos built-in
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # salida 0
print(max(digits)) # salidan 9
print(sum(digits)) # salida 45
