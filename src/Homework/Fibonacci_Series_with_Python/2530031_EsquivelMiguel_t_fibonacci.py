# Fibonacci Series with Python ;)
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
"""
La serie de Fibonacci es una sucesión numérica donde cada término
resulta de sumar los dos anteriores, comenzando con 0 y 1.
Calcular la serie hasta un número de términos n significa generar
los primeros n valores siguiendo esta regla.
El programa cubre la lectura del valor n ingresado por el usuario,
la validación básica de la entrada y la generación de la serie
mostrando los resultados en pantalla.
"""

## Problem: Fibonacci series up to n terms
### Description:
"""
Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, donde n es ingresado por el usuario. La serie debe comenzar en 0 y 1, por lo que:

- Si n = 1 → salida: 0  
- Si n = 2 → salida: 0, 1  
- Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  

El programa debe:
1) Leer n desde la entrada estándar.  
2) Validar n.  
3) Generar la serie de Fibonacci con un bucle (for o while).  
4) Imprimir los términos en una sola línea, separados por espacios o comas.
"""

### Inputs:
"""
- n (int; número de términos de la serie a generar).
"""

### Outputs:
"""
- "Number of terms:" <n> (opcional)
- "Fibonacci series:" <term_1> <term_2> ... <term_n>
"""

### Validations:
"""
- n debe poder convertirse a entero.
- n >= 1.
- (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
- Si la validación falla, NO calcular la serie.
"""
print("Problem: Fibonacci series up to n terms")
try:
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    a = 0
    b = 1
    fibo = [a,b]
    if n > 1:
        print("Number of terms: ", n)
        for i in range(3,n+1):
            fibo.append(fibo[-1] + fibo[-2])
        print("Fibonacci series:",", ".join(map(str, fibo)))
    elif n == 1:
        print("Number of terms: ", n)
        print("Fibonacci series:", a)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem: Fibonacci series up to n terms
Enter the number of terms in the Fibonacci series: 10
Number of terms:  10
Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""
""" 2) Border:
Problem: Fibonacci series up to n terms
Enter the number of terms in the Fibonacci series: 1
Number of terms:  1
Fibonacci series: 0
"""
""" 3) Error:
Problem: Fibonacci series up to n terms
Enter the number of terms in the Fibonacci series:
Error: invalid input
"""

# Conclusiones:
""" 
El uso de un bucle facilitó la generación automática de la serie,
evitando cálculos manuales y asegurando que se pueda extender a cualquier n.
Es importante manejar bien los casos especiales n = 1 y n = 2,
porque garantizan que la salida sea coherente incluso en entradas mínimas.
Esta lógica puede reutilizarse en otros programas que requieran secuencias
numéricas, validaciones de entrada o cálculos iterativos similares.
"""
# Referencias:
"""
CPy. (2023, 22 septiembre). Cómo usar la función map() en Python. CodigosPython. https://codigospython.com/como-usar-la-funcion-map-en-python/
📗 Bucle for en Python. (s. f.). El Libro de Python. https://ellibrodepython.com/for-python
Lifeder. (13 de julio de 2020). Serie de Fibonacci: propiedades, relaciones naturales, aplicaciones. Recuperado de: https://www.lifeder.com/serie-de-fibonacci/.
Lucero, J. A. P. (2022, 20 octubre). Métodos de cadenas split() y join() en Python: Explicados con ejemplos. freeCodeCamp.org. https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/
W3Schools.com. (s. f.-e). https://www.w3schools.com/python/ref_string_join.asp
"""