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
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).
"""
try:
    print("Problem 1: Shopping list basics (list operations)")
    initial_items_text = [item.strip().lower() for item in input("Enter initial items (comma separated): ").split(",") if item.strip()]
    if initial_items_text != [] and initial_items_text != ['']:
        print(initial_items_text)
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

"""
""" 2) Border:

"""
""" 3) Error:

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

### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

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

### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

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

### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

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

### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

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
"""