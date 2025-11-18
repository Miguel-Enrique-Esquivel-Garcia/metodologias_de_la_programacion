cars = ['audi', 'bmw', 'volvo', 'tesla', 'toyota']
for car in cars:
    if car == 'bmw' or car == 'tesla':
        print(car.upper())
    else:
        print(car.lower())

# El condicional es el corazón del if
# Ejemplos de condicionales

# Condicionales True
car_1 = 'bmw'
print("Condicional True: ",car_1 == 'bmw')

# Condicional False
car_2 = "Audi"
print("Condicional False: ", car_2 == 'audi')

car_3 = "Audi"
print(car_3.lower() == "audi")

# Condicional ! = para determinar desigualdad
requested_toppin = "mushrooms"
if requested_toppin != 'anchovies':
    print('Hold the anchovies')

# Comparaciones numéricas
age = 18
print(age==18) # 

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta. Intentalo de nuevo")

age = 19 
print(age<21) #True
print(age<=21) #True
print(age>21) #False
print(age>=21) #False

# Condicionales múltiples
age_0 = 22
age_1 =18
# operación lógica and
print(age_0>=21 and age_1>21) # False
print(age_0>=21 and age_1>=18) #True
# operación lógica or
print(age_0>=22 or age_1>21) # True
print(age_0>=23 or age_1>=21) # False

# Preguntarme si un valor está en una lista
cars = ["micro", "vocho", "tsuru", "tsubaro"]
print("vocho" in cars) # True
print("chevy" in cars) # False

# Preguntarnos si un valor no está una lista
alumnos = ["victor", "ana", "maiki", "gera"]
user = 'josue'

print(user not in alumnos) # True
print("maiki" not in alumnos) # False

# Datos Booleanos
game_active = True
can_edit = False

# If statements
"""
    Programa para pedir la edad a un usuario
    que diga si el  usuario es menor de edad
    o mayor de edad
"""
# try: except: para manejar errores
try:
    edad = input("Por favor ingresa tu edad: ")
    edad = int(edad)
except Exception as err:
    print(err)
    print("No se permiten las letras, ingresa un número entero")
    edad = -1

# if - elif - else
if edad >= 18 and edad < 120:
    print("Eres mayor de edad")
    print("Aguas con que te metan al bote")
elif edad<18 and edad>=0:
    print("Eres menor de edad")
    print("Disfruta tu niñez")
elif edad>=120:
    print("Tienes más de un siglo vivo :O")
else:
    print("Cometiste un error")


print("Programa terminado")

"""
    Ejercicio:
        Elabora un programa que contemple lo siguiente:
            - Si la edad es menor que 4 años, la entrada es gratuita
            - Si la edad está dentro de (4 y 18] años (inclusivo), el costo es de $200
            -Costo para alguien mayor que 18 años es de $500
"""
try:
    user_age = input("Por favor ingresa tu edad: ")
    user_age = int(user_age)
except Exception as e:
    print(e)
    print("No se permiten las letras, ingresa un número")
    user_age = -1

if user_age <= 4 and user_age >=0 or user_age >=65:
    print("Tu entrada es gratuita")
elif user_age > 4 and user_age <= 18:
    print("el costo de su entrada es de $200")
elif user_age > 18 and user_age < 65:
    print("El costo de su entrada es de $500")
else:
    print("Cometiste un error")
print("programa terminado")
# Multiple if-elif-else statements
# else en ocasiones se puede omitr (depende de la situación)
# como se va ejecutando el if-elif-else, una vez que se cumple una condición

## multiple conditions
guisos = ["deshebrada", "salsa verde", "picadillo"]

if "deshebrada" in guisos:
    print("hay deshebrada".upper())
else:
    print("no hay dehebrada".upper())

if "salsa verde" in guisos:
    print("hay salsa verde".swapcase())
else:
    print("no hay salsa verde".swapcase())

if "picadillo" in guisos:
    print("hay picadillo".title())
else:
    print("no hay picadillo".title())

if "mole" in guisos:
    print("Hay Mole")
else:
    print("No hay Mole")

print("\n Guisos en bloque if-elif-else")
guisos = ["deshebrada", "salsa verde", "picadillo"]
if 'deshebrada' in guisos:
    print("hay deshebrada")
elif 'mole' in guisos:
    print("hay mole")
elif 'salsa verde' in guisos:
    print("hay salsa verde")
elif 'picadillo' in guisos:
    print("hay picadillo")

# Lista vacías
guisos = []
if guisos:
    print("Hay guisos disponibles")
else:
    print("No hay guisos disponibles")

## Utilizando dos listas
guisos_disponibles = ["salsa verde", "deshebrada", "picadillo", "huevo con chorizo"]
guisos_a_ordenar = ["barbacoa", "deshebrada", "cabrito"]

print("¿Qué guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"Sí tenemos {guiso}")
    else:
        message_no_guiso = f"""
        Hola soy Charly, de todos los meseros
        el mero, mero, mero
        Lamento informarte que en Cafeteria Jaguares no tenemos {guiso} disponible
        """
        print(message_no_guiso)
print("Realizando pedido...")
print("Gracias por ordenar en Cafeteria Jaguares")