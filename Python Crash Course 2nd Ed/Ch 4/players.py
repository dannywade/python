#Slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])
print(players[:3])
print(players[2:])
print(players[-1:])


#Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on the team:")

for player in players[:3]:
    print(player.title())