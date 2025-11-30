# Fibonacci Series with Python ;)
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
"""
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

try:
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    a = 0
    b = 1
    print("Number of terms: ", n)
    print(a)
    if n > 1:
        print(b)
    for i in range(3,n+1):
        c = a + b
        print (c)
        a = b
        b = c    
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

"""

# Conclusiones:
""" 
"""
# Referencias:
"""
📗 Bucle for en Python. (s. f.). El Libro de Python. https://ellibrodepython.com/for-python
Lifeder. (13 de julio de 2020). Serie de Fibonacci: propiedades, relaciones naturales, aplicaciones. Recuperado de: https://www.lifeder.com/serie-de-fibonacci/.
W3Schools.com. (s. f.-e). https://www.w3schools.com/python/ref_string_join.asp
"""