"""
 Un string es de manera sencilla una serie de caracteres

    En python todo lo que se ENCUENTRE DENTRO DE
    COMILLAS SIMPLES ' ' O DOBLES " "
    es considerado un STRING.

    por ejemplo:

    "Esto es un string"
    'Esto también es un string'

    'Le dije a un amigo, "¡Python es mi lenguaje favorito!"'
    "El lenguaje 'PYTHON' lleva el nombre en honor a Monty Python, no por la Serpiente."

"""

# STRINGS

name = "clase de programación"
print(name)
print( )
print(name.title())  # Convierte la primera letra de cada palabra en mayúscula
print( )
print(name)
print( )

"""
    Un método es una acción de python
    puede realizar en un fragmento de 
    datos o sobre una variable.

    El punto (.) después de la variable string
    seguido del método title() dice que
    se tiene que ejecutar el método title() de
    la variable name.

    Todos los métodos van seguidos de paréntesis
    porque en ocasiones necesitan información
    adicional para funcionar, lo cual iría dentro de los paréntesis.

    En esta ocasión el método .title() no requiere
    información adicional para ejecutarse.

"""

# OTROS MÉTODOS

print("Para mayúsculas: ", name.upper())  # Convierte todo el string en mayúsculas
print("Para minúsculas: ", name.lower())  # Convierte todo el string en minúsculas
print( )

# CONCATTENACIÓN
first_name = "Charly"
last_name = "Mercury"
full_name = first_name + " " + last_name  # El espacio entre comillas es para agregar un espacio entre los nombres
print("Nombre completo: ", full_name)

print("Hola", "¡" + full_name.title() + "!")  # Saludo con nombre completo en mayúscula la primera letra de cada palabra

message = "Hola", "¡" + full_name.title() + "!"
print(message)

"""
f strings
"""
simonname = f"{first_name.title()} {last_name.title()}"
print(simonname)

"""
    Ejercicio:
    Imprime el nombre de un personaje famoso y una cita famoesa de ese personaje.
    Ejemplo:
        Charly Mercury una vez dijo el 103 es mi grupo favorito.
"""
famoso = "Julián Garza"
frase = "Cállate baboso"
cita_famosa = f'{famoso} una vez dijo: "{frase}"'
print(cita_famosa)

famoso2 = "Cristiano Ronaldo"
frase2 = "Muchas gracias a la afición, esto es para vosotros: Siuuuu"
cita_famosa2 = f'{famoso2} una vez dijo: "{frase2}"'
print(cita_famosa2)

# Whitespaces
"""
    Los whitespaces se refiere a cualquier carácter
    que no se imprime, es decir, un escpacio en blanco,
    un tabulador o un salto de línea. Los whitespaces
    se utiliza comunmente para organizar las salidas
    en pantalla de tal manera que sea más amigable
    de leer o ver para los usuarios.
"""
print("\n\nWhitespaces")
print("Python")
print("\tPython")  # Agrega un tabulador antes de la palabra Python
print("\t\tPython")  # Agrega dos tabuladores antes de la palabra Python
print("Lenguages: \nPython\n\t C\n\t\t JavaScript")  # Agrega un salto de línea antes de cada lenguaje

#Eliminación de espacios en Blanco
print("\n\nEliminación de escpacios en Blanco")
favorite_language = "  python  "
print(favorite_language)
print(favorite_language.rstrip())  # Elimina los espacios en blanco a la derecha
print(favorite_language.lstrip())  # Elimina los espacios en blanco a la izquierda
print(favorite_language.strip())   # Elimina los espacios en blanco a ambos lados


# Syntax Error con Strings
print("\n\nSyntax Error con Strings")
message = 'Una fortaleza de Python en su comunidad activa.'
print(message)
# (Error) Error de sintaxis, tienes que pner comillas dobles
message_ = 'Una fortaleza de "Python" en su comunidad activa.'
print(message_)