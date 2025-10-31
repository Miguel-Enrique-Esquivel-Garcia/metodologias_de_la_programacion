message = "This is my first variable!"
another_message = "Variables are used to store information"

print(message)
print(another_message)

print(message, another_message)
print(another_message, message)

"""
    Los nombres de las variables deben nombrarse sólo con:
        - letras, números y guión bajo
        - deben comenzar con una letra o guión bajo
          pero no con números:
          (correcto) message_1, (incorrecto) 1_message
        - no utilizar espacios para separar palabras en variables
        - no utilizar palabras reservadas por python para nombrar variables
        - los nombres deben ser cortos, pero descriptivos
        - letras minúsculas
"""

#
python_message = "Hola amigo Python"
print(python_message, "Charly")
print(python_message, "Mercury")
print(python_message, "Paulo Cohelo")




"""
print(python_mesage)

    Traceback: Es un registro de donde el intérprete tuvo problemas al intentar ejecutar el código.

    ejemplo:
        Traceback (most recent call last):
            File "C:/Usersthepo/python_projects/test_project/src/undestanding_variables.py", line 28, in <module>
            print(python_mesage)
              ^^^^^^^^^^^^^
            NameError: name 'python_mesage' is not defined. Did you mean: 'python_message'?

    NameError: Significa que olvidamos establecer el valor de una
        variable antes de utilizar o que cometimos un error al ingresar
        el nombre de la variable.


"""