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
simple para elementos almacenados en un diccionario cuyas llave
serán las ide y los valores, listas con el resto de elementos, 
usando funciones para cada operación y un menú de texto para interactuar con el usuario.

Implementa un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD. Cada ítem puede representar, por ejemplo, un producto de inventario con los siguientes campos sugeridos:

- id (string o int, único)
- name (string)
- price (float)
- quantity (int)

El programa debe:

1) Definir una estructura de datos principal:
   - Opción A: dict item_id -> dict con datos del ítem.

2) Definir FUNCIONES separadas para cada operación CRUD:
   - create_item(data_structure, item_id, name, price, quantity) -> bool o dict
   - read_item(data_structure, item_id) -> dict o None
   - update_item(data_structure, item_id, new_name, new_price, new_quantity) -> bool
   - delete_item(data_structure, item_id) -> bool
   - list_items(data_structure) -> list o simplemente imprime
   Puedes ajustar nombres y parámetros, pero debe quedar claro qué hace cada función y qué regresa.

3) Implementar un MENÚ en el código principal (main loop):
   Ejemplo de opciones:
   - 1) Create item
   - 2) Read item by id
   - 3) Update item by id
   - 4) Delete item by id
   - 5) List all items
   - 0) Exit

4) En el bucle principal:
   - Mostrar el menú.
   - Leer la opción.
   - Según la opción, pedir los datos necesarios (id, name, price, quantity).
   - Llamar a la función correspondiente.
   - Mostrar mensajes claros de resultado.
"""
### Inputs: 
"""
- User menu options (string or int).
- For CREATE/UPDATE: item_id, name, price, quantity.
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
    if item_id not in data_structure and item_id != "":
        if name != "" and price >= 0.0 and quantity >= 0:
            data_structure[item_id] = [f"Name: {name}", f"Price: {price}", f"Quantity: {quantity}"]

            return True, "Item created"
        else:
            return False, "Error: invalid input"
    else:
        return False, "The item already exists"
def read_item(data_structure, item_id):
    if item_id in data_structure:
        return f"For Item ID {item_id} : {data_structure.get(item_id)}"
    else:
        return None
def update_item(data_structure, item_id, new_name, new_price, new_quantity):
    if item_id in data_structure and item_id != "":
        if new_name != "" and new_price >= 0.0 and new_quantity >= 0:
            data_structure[item_id] = [f"Name: {new_name}", f"Price: {new_price}", f"Quantity: {new_quantity}"]

            return True, "Item updated"
        else:
            return False, "Error: invalid input"
    else:
        return False, "The item not exist"
def delete_item(data_structure, item_id):
    if item_id in data_structure and item_id != "":
        del data_structure[item_id]
        return True, "Item deleted"
    else:
        return False, "The item not exist"
def list_items(data_structure):
    if data_structure == {}:
        return "No items found"
    else:
        print("Items list:")
        for item_id, item in data_structure.items():
            print(f"ID: {item_id}, item : {item}")
        return ""

data_structure = {}
while True:
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")    
    try:
        option = input("Choose an option: ").strip()
        if int(option) == 0:
            print("Exit")
            break
        else:
            if int(option) == 1:
                print("Create an item: ")
                item_id = input("Set the id for the item: ").strip()
                name = input("Set the item's name: ").lower().strip()
                price = float(input("Set the item's price: ").strip())
                quantity = int(input("Set the item's quantity: ").strip())
                quest,text = create_item(data_structure, item_id, name, price, quantity)
                if quest == True:
                    print(text)
                else:
                    print(text)
            elif int(option) == 2:
                print("Read item by id: ")
                item_id = input("Set the id for the item: ").strip()
                read = read_item(data_structure, item_id)
                if read == None:
                    print ("Item not found")
                else:
                    print(read)
            elif int(option) == 3:
                print("Update item by id: ")
                item_id = input("Set the id for the item: ").strip()
                new_name = input("Set the item's new name: ").lower().strip()
                new_price = float(input("Set the item's new price: ").strip())
                new_quantity = int(input("Set the item's new quantity: ").strip())
                questi,textt = update_item(data_structure, item_id, new_name, new_price, new_quantity)
                if questi == True:
                    print(textt)

                else:
                    print(textt)
            elif int(option) == 4:
                print("Delete item by id: ")
                item_id = input("Set the id for the item: ").strip()
                questu,textx = delete_item(data_structure, item_id)
                if questu == True:
                    print(textx)

                else:
                    print(textx)
            elif int(option) == 5:
                print(list_items(data_structure))

    except:
        print("Error: invalid input")
        



### Test cases:
"""
1) Normal: create an item, read it, update it, delete it → expected messages and final state.
Problem: Gestor CRUD usando diccionarios y/o listas con funciones.
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Create an item:
Set the id for the item: 1234
Set the item's name: qwer
Set the item's price: 12
Set the item's quantity: 12
Item created
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Create an item:
Set the id for the item: 1235
Set the item's name: asdd
Set the item's price: 56
Set the item's quantity: 8
Item created
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Create an item:
Set the id for the item: 1236
Set the item's name: khuy
Set the item's price: 4.5
Set the item's quantity: 5
Item created
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 2
Read item by id:
Set the id for the item: 1235
For Item ID 1235 : ['Name: asdd', 'Price: 56.0', 'Quantity: 8']
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 3
Update item by id:
Set the id for the item: 1235
Set the item's new name: poyo
Set the item's new price: 98
Set the item's new quantity: 65
Item updated
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 4
Delete item by id:
Set the id for the item: 1234
Item deleted
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 5
Items list:
ID: 1235, item : ['Name: poyo', 'Price: 98.0', 'Quantity: 65']
ID: 1236, item : ['Name: khuy', 'Price: 4.5', 'Quantity: 5']

1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 0
Exit
2) Border: attempt to create item with minimal valid data (e.g., quantity = 0) y un id muy corto.
Problem: Gestor CRUD usando diccionarios y/o listas con funciones.
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Create an item:
Set the id for the item: 1
Set the item's name: q
Set the item's price: 1
Set the item's quantity: 1
Item created
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Create an item:
Set the id for the item: 0
Set the item's name: 0
Set the item's price: 0
Set the item's quantity: 0
Item created
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 2
Read item by id:
Set the id for the item: 0
For Item ID 0 : ['Name: 0', 'Price: 0.0', 'Quantity: 0']
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 5
Items list:
ID: 1, item : ['Name: q', 'Price: 1.0', 'Quantity: 1']
ID: 0, item : ['Name: 0', 'Price: 0.0', 'Quantity: 0']

1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
3) Error: use invalid menu option, invalid id (empty), or non-numeric price → expected error messages.
Problem: Gestor CRUD usando diccionarios y/o listas con funciones.
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option:
Error: invalid input
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Create an item:
Set the id for the item:
Set the item's name:
Set the item's price:
Error: invalid input
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 2
Read item by id:
Set the id for the item:
Item not found
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 3
Update item by id:
Set the id for the item:
Set the item's new name:
Set the item's new price:
Error: invalid input
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 4
Delete item by id:
Set the id for the item:
The item not exist
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 5
No items found
Choose an option: 1
Create an item:
Set the id for the item:
Set the item's name:
Set the item's price: q
Error: invalid input
"""

# Conclusiones
"""
El uso de funciones permitió organizar el código del CRUD en bloques claros y reutilizables,
lo que simplificó tanto la implementación como el mantenimiento.
El diccionario con listas ofreció flexibilidad para manejar múltiples registros bajo una misma clave,
facilitando búsquedas y actualizaciones rápidas.
Durante la validación de entradas surgieron problemas como valores vacíos o tipos incorrectos,
que se solucionaron aplicando condicionales y manejo de excepciones para asegurar datos consistentes.
Además, este CRUD puede crecer hacia un sistema más robusto integrando persistencia en archivos o bases de datos,
lo que permitiría conservar la información entre ejecuciones y escalar a aplicaciones multiusuario.
En conjunto, la experiencia mostró cómo una buena estructura y validación fortalecen la confiabilidad del programa
y sientan las bases para proyectos más complejos.  
"""

# Referencias
"""
Diccionarios y listas en Python - Tutorial python. (2022, 11 agosto). Tutorial Python. https://tutorialpython.com/listas-en-python/
Fernández, M. (s. f.-b). Acceder a Elementos del Diccionario en Python. https://thedataschools.com/python/diccionarios/acceder-elementos.html
Franciscomelov. (2024, 9 febrero). Operaciones CRUD  – ¿Qué es CRUD? freeCodeCamp.org. https://www.freecodecamp.org/espanol/news/operaciones-crud-que-es-crud/
Yursha, A. (2023b, enero 30). Cómo eliminar un elemento de un diccionario Python. Delft Stack. https://www.delftstack.com/es/howto/python/how-to-remove-an-element-from-a-python-dictionary/
"""