"""
    Estructura básica del bucle while en Python.

    conditional -> bool
    white conditional:
        actions
"""
# try: except:
# While infinito
while True: #While infinito
    try:
        number = int(input("Escribir un número entre 25 y 50: "))
        if number >= 25 and number <= 50:
            print("Hola estás adentro del rango")
            break # Rompe el while
        else:
            print("Lástima Margarito, intenta de nuevo.")
    except:
        print("Carácter inválido")
print("Charly Mercury te saluda")

