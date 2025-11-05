# Numbers - Numéricos Enteros
"""
    Integers

    Los podemos sumar (+), restar (-), multiplicar (*), dividir (/),
    elevar a una potencia (**2, **3, ..., etc), obtener el módulo (%).
"""

number_1 = 35
number_2 = 15
sum = number_1 + number_2
difference = number_1 - number_2
product = number_1 * number_2
quotient = number_1 / number_2
power = number_1 ** 2
modulo = number_1%number_2

print("Suma: ", sum, type(sum))
print("Diferencia: ", difference, type(difference))
print("Producto: ", product, type(product))
print("Cociente: ", quotient,  type(quotient))
print("Potencia (2): ", power, type(power))
print("Módulo: ", modulo, type(modulo))

"""
    Python también respeta la jerarquía de operaciones

    2+3*4 = 14
    (2+3)*4 = 20

"""

# Floats - Numéricos Reales
"""
    Floats

    Lospodemos sumar (+), restar (-), multiplicar (*), dividir (/),
    elevar a una potencia (**2, **3, ..., etc), obtener el módulo (%).

    Python llama Floats a cualquier número con punto decimal.
"""

print("Floats")
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(0.1*2)

"""
    Tomar en cuenta que en ocasiones podemos obtener un número arbitrario
    de números decimales en la respuesta.

    Eso pasa en muchos lenguajes de programación, pero no debemos preocuparnos :).
"""

print(0.2+0.1)
print(3*0.1)

# imprimir la edad de alguien
age = 33
message = "Charly tiene " + str(age) + " años."
print(message)

"""
    TypeError: Pasa cuando Python no puede reconocer
    el tipo de información
    que se está utilizando.

    Built-in Methods para conversión de tipos:
        - str(): Convierte un número en string
        - int(): Convierte un string en número entero
        - float(): Convierte un string en número decimal
"""
message_f = f"Charly tiene {age} años."
print(message_f)