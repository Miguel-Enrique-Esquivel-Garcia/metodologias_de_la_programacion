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

# Looping through all kay-value pairs
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
language is {value.title()}.")