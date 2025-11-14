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