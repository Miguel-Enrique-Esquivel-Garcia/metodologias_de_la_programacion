# Fibonacci Series with Python ;)
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
"""
# Un CRUD es un programa que implementa las operaciones básicas: 
# Create (crear), Read (leer), Update (actualizar) y Delete (eliminar) datos.  
# Se eligió una lista de diccionarios porque permite manejar múltiples registros, 
# cada uno con sus atributos organizados de forma clara y accesible.  
# El uso de funciones ayuda a separar la lógica de cada operación, 
# facilitando la comprensión, el mantenimiento y la reutilización del código.  
# El programa incluye un menú principal que guía al usuario, 
# además de las funciones para crear, leer, actualizar, eliminar y listar elementos.  
# Así se asegura una estructura ordenada y completa para gestionar la información.  
"""

# Problem: In-memory CRUD manager with functions  

###Descripción:
"""
Programa que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) 
simple para elementos almacenados en un diccionario y/o lista, 
usando funciones para cada operación y un menú de texto para interactuar con el usuario.
"""
### Inputs: 
"""
- User menu options (string or int).
- For CREATE/UPDATE: item_id, name, price, quantity (or the fields you define).
- For READ/DELETE: item_id.
"""
### Outputs:
"""
- Messages indicating the result of each operation:
  - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:", etc.
"""
### Validations:
"""
- Menu option must be valid (for example, 0..4 o 0..5 según tu diseño).
- item_id must not be empty.
- Numeric fields must be valid numbers and greater than or equal to 0.
- Disallow creating an item with an id that is already in use (or document tu decisión).
- For READ/UPDATE/DELETE, if the id does not exist, show "Item not found".
"""

print("Problem: Gestor CRUD usando diccionarios y/o listas con funciones.")
def create_item(data_structure, item_id, name, price, quantity):
    return:
def read_item(data_structure, item_id):
    return:
def update_item(data_structure, item_id, new_name, new_price, new_quantity):
    return:
def delete_item(data_structure, item_id):
    return:
def list_items(data_structure):
    return:
almacenated_items = {}
while True:
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")    
    try:
        option = input("Choose an option: ")
        if int(option) == 0:
            break
        else:
            if int(option) == 1:
                print("Simóm")
    except:
        print("Error: invalid input")
        



### Test cases:
"""
1) Normal: create an item, read it, update it, delete it → expected messages and final state.
2) Border: attempt to create item with minimal valid data (e.g., quantity = 0) o usar un id muy corto/largo (documenta tus reglas).
3) Error: use invalid menu option, invalid id (empty), or non-numeric price → expected error messages.
"""

# Conclusiones
"""
El uso de funciones permitió dividir la lógica del CRUD en partes claras, 
haciendo más sencillo entender y mantener el código.  
La lista de diccionarios resultó útil porque cada registro puede almacenar 
múltiples atributos y se accede fácilmente por sus claves.  
Al validar entradas surgieron problemas como valores vacíos o tipos incorrectos, 
que se solucionaron con condicionales y conversiones de datos.  
Esta validación mejoró la robustez del programa y evitó errores en la ejecución.  
El CRUD puede crecer integrando persistencia en archivos (JSON, CSV) o bases de datos, 
lo que permitiría manejar grandes volúmenes de información y múltiples usuarios.  
Así, la estructura básica se convierte en la base de un sistema más completo y escalable.  
"""

# Referencias
"""
"""