"""
Docstring for understanding_functions

Las funciones son bloques de código diseñadas
para realizar una tarea específica.

Cuando queremos realizar la tarea que se ha definido
en una función, simplemente lo que hay que hacer es 
"llamar" el nombre de la función que queremos ejecutar.

"Definición de función" o "Sintaxis general de una función":
"""
# Palabra reservada "def" + nombre de la función + paréntesis + dos puntos
def greeting_paulo():
    """
    Docstring for greeting_paulo

    Esta función saluda a Paulo.
    """
    print("Hello, Paulo!")

greeting_paulo()
greeting_paulo()


"""
    Vamos a hacer una función que pida al usuario
    first_name, middle_name, last_name

    La función debe regresar el nombre completo.
"""
# La función tiene tres parámetros
def create_full_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
    
user_first_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escribe tu segundo nombre: ").strip().lower()
user_last_name = input("Escribe tu apellido: ").strip().lower()

# Argumentos
# Argumentos posicionales
print(create_full_name(user_first_name, user_middle_name, user_last_name))
# Argumentos posicionales
generted_full_name = create_full_name(user_first_name, 
    user_middle_name, user_last_name)
print(generted_full_name)

# Argumentos clave = Keyword Argumenta
full_name_key = create_full_name(
    last_name=user_last_name,
    first_name=user_first_name,
    middle_name=user_middle_name
)

# args, kwergs
# como explorar archivos (DICCIONARIOS, .txt, csv)
# args por consola (sys)
# cli - command linear interfaces
# opp - oriented objects programs
# testing