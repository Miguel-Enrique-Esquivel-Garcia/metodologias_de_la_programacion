# Simple dictionary
alien_0 = {'color':'green','points': 5} #un diccionario tiene llave : valor
print(alien_0['color'])

# The simplest dictionary
alien_1 = {'color':'yellow'}

#Accessing values in the dictionary
print(alien_0['points'])
print(alien_1['color'])

#Empty dictionary
alien_2 = {}
#Modifying values in a dictionary
alien_2 = {'color':'yellow'}
alien_2 ['color'] = 'blue'

# Adding new key-value
alien_2['x_position'] = 0
alien_2['y_position'] = 25

print(alien_2)

## Dictionary to store similar objects
favorite_languages= {
    'jen': 'python' ,
    'sarah': 'c',
    'edward': 'ruby', 
    'phil': 'python',
}

print(f"Sarah favorite language is {favorite_languages['sarah'].title()}.")

# Looping through all key-value pairs
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
language is {value.title()}.")

covenant_grunts = {
    "name" : "grunts",
    "color": "orange", 
    "height": "small", 
    "weapon": "plasma-gun",
    "health": 3,
    "pointd": 1
    }

covenant_elite = {
    "name" : "elite",
    "color": "blue", 
    "height": "big", 
    "weapon": "plasma-sword",
    "health": 6,
    "pointd": 3
    }

covenant_jackal = {
    "name" : "jackal",
    "color": "green",
    "height": "medium",
    "weapon": "plasma-gun",
    "hit-points": 7,
    "health": 3,
    "points": 2
}
for key, value in covenant_grunts.items():
    print(f"{key} : {value}")

# NESTING
# Estudiar - Listas de diccionarios
# Estudiar - Listas en diccionarios
# Estudiar - Diccionario de Diccionarios

## Listas de diccionarios
covenants = [
    covenant_grunts,
    covenant_elite,
    covenant_jackal
]

for aux in covenants:
    print ("\n Covenant: ", aux)
    for key, value in aux.items():
        print(f"{key} : {value}")

## Listas en diccionarios
students = {
    "pablo" : ["cars", "programar en python", "hacer la tarea"],
    "gerardo-pelon" : ["motos", "programar en arduino", "no le gusta hacer la tares"],
    "gerardo-ame" : ["America"]
}
print(students["gerardo-pelon"])

## Diccionarios en diccionarios
sensors = {
    "temperatura": {
        "id": "temp_1",
        "location" : "classroom_a1",
        "value": 20,
    },

    "humidity": {
        "id": "hum_1",
        "location" : "classroom_a2",
        "value": 60,
    }
}

# Imprimir el valor de la temperatura
print("Temperatura")
print(sensors["temperatura"]["value"])
print("ID")
print(sensors["temperatura"]["id"])

# INVESTIGAR El método get() de los diccionarios
mi_diccionario = {"nombre": "Ana", "edad": 25}
## Acceder a una clave existente
print(mi_diccionario.get("nombre"))  # Salida: Ana
## Acceder a una clave inexistente
print(mi_diccionario.get("ciudad"))  # Salida: None
