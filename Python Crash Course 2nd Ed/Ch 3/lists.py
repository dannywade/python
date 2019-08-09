bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

#Modifying a list

#Changing
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding/Appending
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#Adding/Appending
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(1, 'ducati')
print(motorcycles)

#Deleting/Removing
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#del 
del motorcycles[0]
print(motorcycles)

#pop()
popped = motorcycles.pop()
print(motorcycles)

#remove()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")