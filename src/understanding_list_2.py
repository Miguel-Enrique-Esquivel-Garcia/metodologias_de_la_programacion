"""
    Slicing a list to obtain a sublist.
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Lista original de los jugadores: ", players)
print("Los primeros 3 jugadores son:")
print("Slicing", players[0:3]) #-> ['charles', 'martina', 'michael']

print("Slice: ", players[1:4]) #-> ['martina', 'michael', 'florence']
print("Los primeros 4 jugadores son:" , players[:4]) #-> ['charles', 'martina', 'michael', 'florence']
print("Los jugadores desde el tercero hasta el final son:" , players[2:]) #-> ['michael', 'florence', 'eli']
print("Los últimos 3 jugadores son:" , players[-3:]) #-> ['michael', 'florence', 'eli']

# Slicing en un for loop
print("Imprime los primeros 3 jugadores usando un for loop:")
for player in players[0:3]:
    print(player.title())


# Copiar una lista completa usando slicing
## my_players = players <- ERROR así no se copia una lista
my_players = players[:]  # Copia completa de la lista players
print("Lista copiada de jugadores: ", my_players)
players_2 = list(players)  # Otra forma de copiar una lista
print("Otra lista copiada de jugadores: ", players_2)
players_3 = players.copy()  # Otra forma de copiar una lista
print("Otra lista copiada de jugadores: ", players_3)

cars = ["bwm", "toyota", "volkswagen", "porche"]
print(cars)
cars[0] = "bmw"
cars[3] = "porsche"
print(cars)