# Manejo de funciones en Python
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
"""
Una función en Python es un bloque de código que realiza una tarea específica y puede reutilizarse.
Los parámetros se definen al crear la función y sirven como variables de entrada,
mientras que los argumentos son los valores concretos que se pasan al llamar la función.
Separar la lógica en funciones reutilizables permite organizar mejor el código y evitar repeticiones.
Un valor de retorno es el resultado que la función entrega al finalizar su ejecución.
Es preferible devolver resultados en lugar de solo imprimirlos, porque así pueden usarse en otros cálculos.
El documento cubrirá la descripción de cada problema y el diseño de las funciones necesarias.
También incluirá las entradas y salidas esperadas, junto con validaciones para asegurar datos correctos.
Finalmente, se presentarán pruebas básicas que demuestran el correcto funcionamiento de las soluciones.
"""
## Principios y Buenas Prácticas:
"""
- Preferir funciones pequeñas que hagan una sola cosa (single responsibility).
- Evitar repetir código: si copias/pegas lógica, considera extraerla en una función.
- Intentar que las funciones sean “puras” cuando sea posible (mismo input -> mismo output, sin efectos secundarios externos).
- Documentar con comentarios simples qué hace cada función y qué parámetros espera.
- Dar nombres claros a las funciones (calculate_bmi, not f1 o do_it).
"""

# Problemas
## Problem 1: Rectangle area and perimeter (basic functions)
### Description:
"""
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.
"""
### Inputs:
"""
width (float)
height (float)
"""
### Outputs:
"""
"Area:" <area_value>
"Perimeter:" <perimeter_value>
"""
### Validations:
"""
width > 0
height > 0
Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.
"""

print("Problem 1: Rectangle area and perimeter (basic functions)")
def calculate_area(width, height):
    """
    Returns the area of a rectangle
    """
    area = width * height
    return area
def calculate_perimeter(width, height):
    """
    Returns the perimeter of a rectangle
    """
    perimeter = 2 * (width + height)
    return perimeter
try:
    width = float(input("Set the width of the rectangle: "))
    height = float(input("Set the height of the rectangle: "))
    if width > 0 and height > 0:
        area_value = calculate_area(width, height)
        print("Area: ", area_value)
        perimeter_value = calculate_perimeter(width, height)
        print("Perimeter: ", perimeter_value)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 1: Rectangle area and perimeter (basic functions)
Set the width of the rectangle: 5
Set the height of the rectangle: 30
Area:  150.0
Perimeter:  70.0
"""
""" 2) Border:
Problem 1: Rectangle area and perimeter (basic functions)
Set the width of the rectangle: 0.1
Set the height of the rectangle: 0.1
Area:  0.010000000000000002
Perimeter:  0.4
"""
""" 3) Error:
Problem 1: Rectangle area and perimeter (basic functions)
Set the width of the rectangle:
Error: invalid input
"""

## Problem 2: Grade classifier (function with return string)
### Description:
"""
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.
"""
### Inputs:
"""
score (float o int)
"""
### Outputs:
"""
"Score:" <score>
"Category:" <grade_letter>
"""
### Validations:
"""
0 <= score <= 100
Si no se cumple, mostrar "Error: invalid input" y no clasificar.
"""

print("Problem 2: Grade classifier (function with return string)")
def classify_grade(score):
    if score >= 90:
        grade_letter = "A"
        return grade_letter
    elif score >= 80 and score < 90:
        grade_letter = "B"
        return grade_letter
    elif score >= 70 and score < 80:
        grade_letter = "C"
        return grade_letter
    elif score >= 60 and score < 70:
        grade_letter = "D"
        return grade_letter
    elif score < 60:
        grade_letter = "F"
        return grade_letter

try:
    score = int(input("Score a number from 0-100: "))
    if score >= 0 and score <= 100:
        grade_letter = classify_grade(score)
        print("Score: ", score)
        print("Category: ", grade_letter)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")


### Test cases.
""" 1) Normal:
Problem 2: Grade classifier (function with return string)
Score a number from 0-100: 100
Score:  100
Category:  A
"""
""" 2) Border:
Problem 2: Grade classifier (function with return string)
Score a number from 0-100: 0
Score:  0
Category:  F
"""
""" 3) Error:
Problem 2: Grade classifier (function with return string)
Score a number from 0-100:
Error: invalid input
"""

## Problem 3: List statistics function (min, max, average)
### Description:
"""
Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), 
llamar la función y mostrar los valores.
"""
### Inputs:
"""
numbers_text (string; por ejemplo, "10,20,30")
Internamente: numbers_list (list of float o int)
"""
### Outputs:
"""
"Min:" <min_value>
"Max:" <max_value>
"Average:" <average_value>
"""
### Validations:
"""
numbers_text no vacío tras strip().
Lista no vacía después de la conversión.
Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".
"""

print("Problem 3: List statistics function (min, max, average)")
def summarize_numbers(numbers_list):
    """
    Returns a dictionary with min, max and average of a list of numbers
    """
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }
numbers_text = input("Set numbers separated by commas: ").strip()
if numbers_text != "":
    try:
        numbers_list = [float(num.strip()) for num in numbers_text.split(",")]
        if numbers_list != []:
            values = summarize_numbers(numbers_list)
            print("Min: ", values["min"])
            print("Max: ", values["max"])
            print("Average: ", values["average"])
        else:
            print("Error: invalid input")
    except ValueError:
        print("Error: invalid input")
else:
    print("Error: invalid input")



### Test cases.
""" 1) Normal:
Problem 3: List statistics function (min, max, average)
Set numbers separated by commas: 10,12,11,13,11,12,10,11,13,14
Min:  10.0
Max:  14.0
Average:  11.7
"""
""" 2) Border:
Set numbers separated by commas: 0,0,0,0,0,0,0
Min:  0.0
Max:  0.0
Average:  0.0
"""
""" 3) Error:
Problem 3: List statistics function (min, max, average)
Set numbers separated by commas:
Error: invalid input
"""

## Problem 4: Apply discount list (pure function)
### Description:
"""
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.
"""
### Inputs:
"""
prices_text (string; por ejemplo, "100,200,300")
discount_rate (float, entre 0 y 1)
"""
### Outputs:
"""
"Original prices:" <original_list>
"Discounted prices:" <discounted_list>
"""
### Validations:
"""
prices_text no vacío y lista resultante no vacía.
Todos los precios > 0.
0 <= discount_rate <= 1; si no, "Error: invalid input"
"""

print("Problem 4: Apply discount list (pure function)")
def apply_discount(prices_list, discount_rate):
    """
    Returns the price list with discount
    """
    return [price * (1-discount_rate) for price in prices_list]
    
prices_text = input("Set prices separated by commas: ").strip()
discount_rate = input("Set the discount rate: ").strip()
if prices_text != "" and discount_rate != "":

    try:
        prices_list = [float(prices.strip()) for prices in prices_text.split(",")]
        discount_rate = float(discount_rate)
        if prices_list != [] and all(price > 0 for price in prices_list) and discount_rate >= 0 and discount_rate <= 1:
            discounted_list = apply_discount(prices_list, discount_rate)
            print("Original prices: ", prices_list)
            print("Discounted prices: ", discounted_list)
        else:
            print("Error: invalid input")
    except:
        print("Error: invalid input")
else:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 4: Apply discount list (pure function)
Set prices separated by commas: 12,2,90,100,1000
Set the discount rate: 0.5
Original prices:  [12.0, 2.0, 90.0, 100.0, 1000.0]
Discounted prices:  [6.0, 1.0, 45.0, 50.0, 500.0]
"""
""" 2) Border:
Problem 4: Apply discount list (pure function)
Set prices separated by commas: 1
Set the discount rate: 1
Original prices:  [1.0]
Discounted prices:  [0.0]
"""
""" 3) Error:
Problem 4: Apply discount list (pure function)
Set prices separated by commas:
Set the discount rate:
Error: invalid input
"""

## Problem 5: Greeting function with default parameters
### Description:
"""
Define una función greet(name, title="") que:
- Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
- Regrese el mensaje: "Hello, <full_name>!"
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.
"""
### Inputs:
"""
name (string)
title (string opcional)
"""
### Outputs:
"""
"Greeting:" <greeting_message>
"""
### Validations:
"""
name no vacío tras strip().
title puede estar vacío, pero si no lo está, también se normaliza con strip().
"""

print("Problem 5: Greeting function with default parameters")
def greet(name, title=""):
    full_name = f"{title} {name}".strip()
    return f'"Hello, {full_name}!"'
try:
    name = input("Set your name: ").strip().title()
    title = input("Set your academic title: ").strip().title()
    if name != "":
        greeting_message = greet(name, title)
        print("Greeting: ", greeting_message)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 5: Greeting function with default parameters
Set your name: Liborio
Set your academic title: Dr.
Greeting:  "Hello, Dr. Liborio!"
"""
""" 2) Border:
Problem 5: Greeting function with default parameters
Set your name: Pepito
Set your academic title:
Greeting:  "Hello, Pepito!"
"""
""" 3) Error:
Problem 5: Greeting function with default parameters
Set your name:
Set your academic title:
Error: invalid input
"""

## Problem 6: Factorial function (iterative or recursive)
### Description:
"""
Define una función factorial(n) que regrese n! (n factorial). 
Puedes implementarla de forma iterativa (con for). 
El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.
"""
### Inputs:
"""
n (int)
"""
### Outputs:
"""
"n:" <n>
"Factorial:" <factorial_value>
"""
### Validations:
"""
n entero.
n >= 0.
"""

print("Problem 6: Factorial function (iterative or recursive)")
def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial
try:
    n = int(input("Set a number: "))
    if n >= 0:
        factorial_value = factorial(n)
        print("n: ", n)
        print("Factorial: ", factorial_value)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")


### Test cases.
""" 1) Normal:
Problem 6: Factorial function (iterative or recursive)
Set a number: 10
n:  10
Factorial:  3628800
"""
""" 2) Border:
Problem 6: Factorial function (iterative or recursive)
Set a number: 0
n:  0
Factorial:  1
"""
""" 3) Error:
Problem 6: Factorial function (iterative or recursive)
Set a number:
Error: invalid input
"""


# Conclusiones:
""" 
Las funciones permiten organizar el código en bloques claros y reutilizables,
evitando repetir instrucciones y facilitando la lectura.
Usar return en lugar de solo imprimir da la ventaja de reutilizar los valores
en otros cálculos o procesos, aumentando la versatilidad del programa.
Los parámetros y valores por defecto hacen el código más flexible,
ya que permiten adaptar la función a distintos escenarios sin modificarla.
Encapsular lógica en funciones fue especialmente útil en cálculos repetidos
y validaciones, reduciendo errores y simplificando el flujo principal.
Aprendí que la lógica “principal” coordina la interacción con el usuario,
mientras que las funciones de apoyo se encargan de tareas específicas,
logrando un programa más modular y fácil de mantener.
"""
# Referencias:
"""
Bustamante, S. J. (2021, 21 febrero). Guía de funciones de Python con ejemplos. freeCodeCamp.org. https://www.freecodecamp.org/espanol/news/guia-de-funciones-de-python-con-ejemplos/
Byspel - Iván L. (2021, 14 agosto). 🔴 CALCULAR FACTORIAL de un NUMERO 🐍 FACTORIAL en Python con CICLO FOR | CURSO DE PYTHON [Vídeo]. YouTube. https://www.youtube.com/watch?v=bfK7Kyc4mwg
Eliz. (2024, 8 noviembre). Grados Académicos en México | Clasificación y Sinónimo en Inglés. Mextudia. https://mextudia.com/los-grados-academicos-en-mexico/
Min() y max() de Python: encontrar valores más pequeños y más grandes. (s. f.-b). https://es.python-3.com/?p=149
Python .split() - Dividir una cadena en Python. (s. f.). https://es.python-3.com/?p=2782
"""