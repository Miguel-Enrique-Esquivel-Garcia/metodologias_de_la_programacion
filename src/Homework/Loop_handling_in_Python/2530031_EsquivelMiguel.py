# Manejo de bucles en Python
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
"""
Un bucle for permite recorrer secuencias (listas, rangos, cadenas) y se usa para repetir acciones
un número conocido de veces o sobre cada elemento de una colección.
Un bucle while ejecuta instrucciones mientras se cumpla una condición lógica, siendo más natural
cuando no sabemos cuántas repeticiones habrá y dependemos de una condición dinámica.
Un contador es una variable que incrementa en cada iteración para llevar registro de la cantidad
de veces que ocurre algo; un acumulador suma valores para obtener un total o resultado agregado.
Es fundamental definir correctamente la condición de salida para evitar ciclos infinitos que
bloqueen el programa y consuman recursos innecesarios.
El documento cubrirá: descripción de cada problema, diseño de entradas y salidas, validaciones
necesarias, y ejemplos del uso de for y while en distintas situaciones como recorridos de datos,
construcción de menús interactivos y lectura repetida de información hasta cumplir una condición.
"""
## Principios y Buenas Prácticas:
"""
- Usar for cuando conoces de antemano cuántas iteraciones necesitas (por ejemplo, 1 a 10).
- Usar while cuando la cantidad de iteraciones depende de una condición (por ejemplo, leer hasta que el usuario escriba "EXIT").
- Inicializar correctamente contadores y acumuladores antes del bucle.
- Actualizar las variables de control dentro del bucle while para no crear ciclos infinitos.
- Mantener el cuerpo del bucle lo más simple posible; extraer lógica compleja en funciones si es necesario.
"""

# Problemas
## Problem 1: Sum of range with for
### Description:
"""
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). 
Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.
"""
### Inputs:
"""
n (int; límite superior del rango).
"""
### Outputs:
"""
"Sum 1..n:" <total_sum>
"Even sum 1..n:" <even_sum>
"""
### Validations:
"""
Verificar que n pueda convertirse a int.
n >= 1; si no se cumple, mostrar "Error: invalid input".
"""

print("Problem 1: Sum of range with for")
try:
    n = int(input("Set the upper limit of the range: "))
    if n >= 1:
        total_sum = 0
        for x in range(1,n+1):
            total_sum += x
        print(f"Sum 1..n: {total_sum}")
        even_sum = 0
        for xp in range(2,n+1,2):
            even_sum += xp
        print("Even sum 1..n:", even_sum)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 1: Sum of range with for
Set the upper limit of the range: 10
Sum 1..n: 55
Even sum 1..n: 30
"""
""" 2) Border:
Problem 1: Sum of range with for
Set the upper limit of the range: 1
Sum 1..n: 1
Even sum 1..n: 0
"""
""" 3) Error:
Problem 1: Sum of range with for
Set the upper limit of the range:
Error: invalid input
"""

## Problem 2: Multiplication table with for
### Description:
"""
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. 
Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
"""
### Inputs:
"""
base (int)
m (int; límite de la tabla)
"""
### Outputs:
"""
Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.
"""
### Validations:
"""
base y m convertibles a int.
m >= 1; si no, "Error: invalid input".
"""

print("Problem 2: Multiplication table with for")
try:
    base = int(input("Set the base number for multiplication table: "))
    m = int(input("Set the table limit: "))
    if m >= 1:
        product = 0
        for x in range(1,m+1):
            product = x * base
            print(f'"{base} x {x} = {product}"')
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 2: Multiplication table with for
Set the base number for multiplication table: 5
Set the table limit: 10
"5 x 1 = 5"
"5 x 2 = 10"
"5 x 3 = 15"
"5 x 4 = 20"
"5 x 5 = 25"
"5 x 6 = 30"
"5 x 7 = 35"
"5 x 8 = 40"
"5 x 9 = 45"
"5 x 10 = 50"
"""
""" 2) Border:
Problem 2: Multiplication table with for
Set the base number for multiplication table: 0
Set the table limit: 1
"0 x 1 = 0"
"""
""" 3) Error:
Problem 2: Multiplication table with for
Set the base number for multiplication table:
Error: invalid input
"""

## Problem 3: Average of numbers with while and sentinel
### Description:
"""
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.
"""
### Inputs:
"""
number (float; se lee repetidamente).
sentinel_value (fijo en el código, por ejemplo: -1).
"""
### Outputs:
"""
"Count:" <count>
"Average:" <average_value>
Si no se ingresan datos válidos:
 - "Error: no data"
"""
### Validations:
"""
Cada lectura debe intentar convertirse a float.
Ignorar el sentinela en los cálculos.
"""

print("Problem 3: Average of numbers with while and sentinel")
count = 0
sum_values = 0.0
sentinel_value = input("Set a sentinel value: ")
while True:
    number = input("Set a number: ")
    if number == sentinel_value:
        break
    try:
        number = float(number)
    except:
        print("Error: no data")
        continue
    count += 1
    sum_values += number
if count == 0:
    print("Error: no data")
else:
    average_value = sum_values/count
    print("Count: ", count)
    print("Average: ", average_value)


### Test cases.
""" 1) Normal:
Problem 3: Average of numbers with while and sentinel
Set a sentinel value: -1
Set a number: 10
Set a number: 10
Set a number: 11
Set a number: 11
Set a number: 11
Set a number: 12
Set a number: 12
Set a number: 13
Set a number: 13
Set a number: 14
Set a number: -1
Count:  10
Average:  11.7
"""
""" 2) Border:
Problem 3: Average of numbers with while and sentinel
Set a sentinel value: -1
Set a number: 0
Set a number: -1
Count:  1
Average:  0.0
"""
""" 3) Error:
Problem 3: Average of numbers with while and sentinel
Set a sentinel value: -1
Set a number: -1
Error: no data
"""

## Problem 4: Password attempts with while
### Description:
"""
Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. 
Si agota los intentos, mostrar un mensaje de bloqueo.
"""
### Inputs:
"""
user_password (string; se lee en cada intento).
"""
### Outputs:
"""
Si acierta:
 - "Login success"
Si falla todos los intentos:
 - "Account locked"
"""
### Validations:
"""
MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
Contar correctamente los intentos.
"""

print("Problem 4: Password attempts with while")
counter = 0
MAX_ATTEMPTS = 3
password = "admin123"
while True:
    user_password = input("Set the password: ")
    if user_password == password:
        print("Login success")
        break
    counter += 1
    if counter < MAX_ATTEMPTS:
        print("Try again")
    if counter == MAX_ATTEMPTS:
        print("Account locked")
        break

### Test cases.
""" 1) Normal:
Problem 4: Password attempts with while
Set the password: admin123
Login success
"""
""" 2) Border:
Problem 4: Password attempts with while
Set the password: .- -.. -- .. -. .---- ..--- ...--
Try again
Set the password: 61,64,6d,69,6e,31,32,33
Try again
Set the password: admin123
Login success
"""
""" 3) Error:
Problem 4: Password attempts with while
Set the password:
Try again
Set the password:
Try again
Set the password:
Account locked
"""

## Problem 5: Simple menu with while
### Description:
"""
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú hasta que se elija 0.
"""
### Inputs:
"""
option (string o int; elección del usuario).
"""
### Outputs:
"""
Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
Para opciones inválidas:
  - "Error: invalid option"

"""
### Validations:
"""
Normalizar option (por ejemplo, convertir a int con manejo de error).
Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.
"""

print("Problem 5: Simple menu with while")
counter_value = 0
print(
        "1) Show greeting\n",
        "2) Show current counter value\n",
        "3) Increment counter\n",
        "0) Exit"
    )
while True:
    option = input("Enter an option: ").strip()
    if option == "1":
        print("Hello!")
    elif option == "2":
        print("Counter: ", counter_value)
    elif option == "3":
        counter_value += 1
        print("Counter incremented")
    elif option == "0":
        print("Bye!")
        break
    else:
        print("Error: invalid option")

### Test cases.
""" 1) Normal:
Problem 5: Simple menu with while
1) Show greeting
 2) Show current counter value
 3) Increment counter
 0) Exit
Enter an option: 1
Hello!
Enter an option: 3
Counter incremented
Enter an option: 2
Counter:  1
Enter an option: 0
Bye!
"""
""" 2) Border:
Problem 5: Simple menu with while
1) Show greeting
 2) Show current counter value
 3) Increment counter
 0) Exit
Enter an option: 0
Bye!
"""
""" 3) Error:
Problem 5: Simple menu with while
1) Show greeting
 2) Show current counter value
 3) Increment counter
 0) Exit
Enter an option: a
Error: invalid option
Enter an option: x
Error: invalid option
Enter an option: 0
Bye!
"""

## Problem 6: Pattern printing with nested loops
### Description:
"""
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
"""
### Inputs:
"""
n (int; número de filas del patrón).
"""
### Outputs:
"""
Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
"""
### Validations:
"""
n convertible a int.
n >= 1; si no, "Error: invalid input".
"""

print("Problem 6: Pattern printing with nested loops")
try:
    n = int(input("Set the pattern height: "))
    if n >= 1:
        asterisks = ""
        for i in range(1,n+1):
            asterisks += "*"
            print(f'"{asterisks}"')
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 6: Pattern printing with nested loops
Set the pattern height: 5
"*"
"**"
"***"
"****"
"*****"
"""
""" 2) Border:
Problem 6: Pattern printing with nested loops
Set the pattern height: 1
"*"
"""
""" 3) Error:
Problem 6: Pattern printing with nested loops
Set the pattern height:
Error: invalid input
"""

# Conclusiones:
""" 
Los bucles for son más útiles cuando sabemos cuántas veces se repetirá el ciclo,
mientras que los bucles while se emplean cuando la condición depende de un evento externo.
Los contadores y acumuladores ayudan a controlar las iteraciones y a sumar o registrar valores.
Un riesgo común en while es caer en ciclos infinitos si no se define bien la condición de salida.
Los menús interactivos y los intentos de contraseña son ejemplos típicos de bucles while.
Los bucles anidados permiten generar patrones y estructuras más complejas, como tablas o figuras.
En general, el uso correcto de bucles mejora la eficiencia y claridad de los programas.
"""
# Referencias:
"""
Franciscomelov. (2022, 7 enero). Tutorial de f-strings en Python: Formato de cadenas en Python explicado con ejemplos. freeCodeCamp.org. https://www.freecodecamp.org/espanol/news/tutorial-de-f-strings-en-python-formato-de-cadenas-en-python-explicado-con-ejemplos/
Losapuntesde. (2025, 8 septiembre). 🔥 Operadores aritméticos y de asignación en Python. Apuntes de Programador. https://apuntes.de/python/operadores-aritmeticos-y-de-asignacion-en-python/#gsc.tab=0
Navarro, S. (2024, 23 mayo). Hacer un contador en Python con 'while' y 'for' KeepCoding Bootcamps. https://keepcoding.io/blog/hacer-un-contador-en-python-con-while-y-for/
📗 Range en Python. (s. f.). El Libro de Python. https://ellibrodepython.com/range-python
Tuxskar. (2025, 30 octubre). Bucles en Python: for y while – Guía completa [+Ejemplos]. El Pythonista. https://elpythonista.com/bucles-en-python-for-y-while-guia-completa-2025-ejemplos
while loop - sentinel value | Python Classroom. (s. f.). Python Classroom. https://www.pythonclassroom.com/loops/while-loop-sentinel
"""