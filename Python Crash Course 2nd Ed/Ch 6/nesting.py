alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'blue', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Nesting
aliens = [alien_0, alien_1, alien_2]

alien_list = []

# Make 30 new aliens
for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    alien_list.append(new_alien)

# Prints all aliens in alien_list
for alien in alien_list:
    print(alien)

print(f"Total number of aliens: {len(alien_list)}")


# Changing properties of the first 3 aliens
for alien in alien_list[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10