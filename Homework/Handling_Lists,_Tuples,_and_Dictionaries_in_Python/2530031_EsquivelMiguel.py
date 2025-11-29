# Manejo de Listas, Tuplas y Diccionarios en Python
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
"""
"""
## Principios y Buenas Prácticas:
"""
- Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, fechas, configuraciones fijas).
- Usar diccionarios cuando necesites buscar información por una clave (por ejemplo, por nombre, id, código).
- Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
- Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "age", "price").
- Escribir código legible y mensajes claros para el usuario.
"""
# Problemas
## Problem 1: Shopping list basics (list operations)
### Description:
"""
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).
"""
### Inputs:
"""
- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).
"""
### Outputs:
"""
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false
"""
### Validations:
"""
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
"""
try:
    print("Problem 1: Shopping list basics (list operations)")
    initial_items_text = [item.strip().lower() for item in input("Enter initial items (comma separated): ").split(",") if item.strip()]
    if initial_items_text != [] and initial_items_text != ['']:
        new_item = input("Add a new item in the list: ")
        new_item = new_item.strip().lower()
        initial_items_text.append(new_item)
        items_list = initial_items_text
        total_items = len(items_list)
        search_item = input("Search in the list: ").lower().strip()
        if search_item in items_list:
            found_item = True
        else:
            found_item = False
        print("Items list: ", items_list)
        print("Total items: ", total_items)
        print("Found item: ", found_item)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 1: Shopping list basics (list operations)
Enter initial items (comma separated): cd,c60,lp
Add a new item in the list: usb
Search in the list: cd
Items list:  ['cd', 'c60', 'lp', 'usb']
Total items:  4
Found item:  True
"""
""" 2) Border:
Problem 1: Shopping list basics (list operations)
Enter initial items (comma separated):  Ronaldo_7 , Messi_10 , Suárez_9
Add a new item in the list: Neymar_11
Search in the list: Modric_10
Items list:  ['ronaldo_7', 'messi_10', 'suárez_9', 'neymar_11']
Total items:  4
Found item:  False
"""
""" 3) Error:
Problem 1: Shopping list basics (list operations)
Enter initial items (comma separated):
Error: invalid input
"""

## Problem 2: Points and distances with tuples
### Description:
"""
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.
"""
### Inputs:
"""
- x1, y1, x2, y2 (float; coordenadas de los puntos).
"""
### Outputs:
"""
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)
"""
### Validations:
"""
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.
"""

print("Problem 2: Points and distances with tuples")
try:
  print("Coordinates of point A")
  x1 = float(input("Set x1: "))
  y1 = float(input("Set y1: "))
  point_a = (x1, y1)
  print("Coordinates of point B")
  x2 = float(input("Set x2: "))
  y2 = float(input("Set y2: "))
  point_b = (x2, y2)
  distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
  mx = (x1 + x2)/2
  my = (y1 + y2)/2
  midpoint = (mx,my)
  print("Point A: ", point_a)
  print("Point B: ", point_b)
  print("Distance: ", distance)
  print("Midpoint: ", midpoint)
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 2: Points and distances with tuples
Coordinates of point A
Set x1: 6
Set y1: 1
Coordinates of point B
Set x2: -1
Set y2: 4
Point A:  (6.0, 1.0)
Point B:  (-1.0, 4.0)
Distance:  7.615773105863909
Midpoint:  (2.5, 2.5)
"""
""" 2) Border:
Problem 2: Points and distances with tuples
Coordinates of point A
Set x1: 0
Set y1: 0
Coordinates of point B
Set x2: 0
Set y2: 0
Point A:  (0.0, 0.0)
Point A:  (0.0, 0.0)
Distance:  0.0
Midpoint:  (0.0, 0.0)
"""
""" 3) Error:
Problem 2: Points and distances with tuples
Coordinates of point A
Set x1: aw
Error: invalid input
"""

## Problem 3: Product catalog with dictionary
### Description:
"""
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.
"""
### Inputs:
"""
- product_name (string).
- quantity (int; cantidad a comprar).
"""
### Outputs:
"""
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"
"""
### Validations:
"""
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).
"""

print("Problem 3: Product catalog with dictionary")
try:
  product_catalog = {"accordion":25385.75,
                     "bajo_sexto":11950.00,
                     "tololoche":15000.50,
                     "saxophone":25000.99,
                     "guitarra":8999.90}
  product_name = input("Enter product name: ").strip().lower()
  if product_name in product_catalog.keys():
      quantity = int(input("Enter the quantity to buy: "))
      if quantity > 0:
          unit_price = product_catalog[product_name]
          total_price = unit_price * quantity
          print("Unit price: ", unit_price)
          print("Quantity: ", quantity)
          print("Total: ", total_price)
      else:
          print("Error: invalid input")
  elif product_name == "":
      print("Error: invalid input")
  else:
      print("Error: product not found")
except:
  print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 3: Product catalog with dictionary
Enter product name: tololoche
Enter the quantity to buy: 2
Unit price:  15000.5
Quantity:  2
Total:  30001.0
"""
""" 2) Border:
Problem 3: Product catalog with dictionary
Enter product name: bajo_sexto
Enter the quantity to buy: 0
Error: invalid input
"""
""" 3) Error:
Problem 3: Product catalog with dictionary
Enter product name:
Error: invalid input
"""

## Problem 4: Student grades with dict and list
### Description:
"""
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.
"""
### Inputs:
"""
- student_name (string).
"""
### Outputs:
"""
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"
"""
### Validations:
"""
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.
"""

print("Problem 4: Student grades with dict and list")
try:
  grades_dict_list = {
      "Mickey" : [100, 100, 100],
      "Pablo" : [10, 100, 75],
      "Gera" : [100, 100, 100],
      "Nana" : [75, 100, 45],
      "Milo" : [10, 70, 70],
  }
  student_name = (input("Enter student name: ")).strip().title()
  if student_name in grades_dict_list.keys():
      average = sum(grades_dict_list[student_name])/len(grades_dict_list[student_name])
      if average >= 70:
          is_passed = True
          print("Grades: ", grades_dict_list[student_name])
          print("Average: ", average)
          print("Passed: ", is_passed)
      else:
          is_passed = False
          print("Grades: ", grades_dict_list[student_name])
          print("Average: ", average)
          print("Passed: ", is_passed) 
  elif student_name == "":
      print("Error: invalid input")
  else:
      print("Error: student not found")
except:
  print("Error: invalid input")



### Test cases.
""" 1) Normal:
Problem 4: Student grades with dict and list
Enter student name: Mickey
Grades:  [100, 100, 100]
Average:  100.0
Passed:  True
"""
""" 2) Border:
Problem 4: Student grades with dict and list
Enter student name: 2530031
Error: student not found
"""
""" 3) Error:
Problem 4: Student grades with dict and list
Enter student name:
Error: invalid input
"""

## Problem 5: Word frequency counter (list + dict)
### Description:
"""
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.
"""
### Inputs:
"""
- sentence (string).
"""
### Outputs:
"""
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)
"""
### Validations:
"""
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.
"""

print("Problem 5: Word frequency counter (list + dict)")
sentence = input("Enter a sentence: ").strip()
if sentence != "":
    sentence = sentence.lower()
    words_list = sentence.split()
    freq_dict = {}
    for word in words_list:
      if word in freq_dict: 
        freq_dict[word] += 1
      else: 
        freq_dict[word] = 1
    most_common_word = max(freq_dict, key=freq_dict.get)
    print("Words list: ", words_list)
    print("Frequencies: ", freq_dict)
    print("Most common word: ", most_common_word)
else:
    print("Error: invalid input")
    


### Test cases.
""" 1) Normal:
Problem 5: Word frequency counter (list + dict)
Enter a sentence: se la robé y me la robaron se la quité y me la quitaron
Words list:  ['se', 'la', 'robé', 'y', 'me', 'la', 'robaron', 'se', 'la', 'quité', 'y', 'me', 'la', 'quitaron']
Frequencies:  {'se': 2, 'la': 4, 'robé': 1, 'y': 2, 'me': 2, 'robaron': 1, 'quité': 1, 'quitaron': 1}
Most common word:  la
"""
""" 2) Border:
Problem 5: Word frequency counter (list + dict)
Enter a sentence: pepe pecas pica papas con un pico
Words list:  ['pepe', 'pecas', 'pica', 'papas', 'con', 'un', 'pico']
Frequencies:  {'pepe': 1, 'pecas': 1, 'pica': 1, 'papas': 1, 'con': 1, 'un': 1, 'pico': 1}
Most common word:  pepe
"""
""" 3) Error:
Problem 5: Word frequency counter (list + dict)
Enter a sentence:
Error: invalid input
"""

## Problem 6: Simple contact book (dictionary CRUD)
### Description:
"""
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.
"""
### Inputs:
"""
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").
"""
### Outputs:
"""
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"
"""
### Validations:
"""
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().
"""

print("Problem 6: Simple contact book (dictionary CRUD)")

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
W3Schools.com. (s. f.-c). https://www.w3schools.com/python/ref_dictionary_keys.asp
"""