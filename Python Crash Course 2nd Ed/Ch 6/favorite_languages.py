# Putting a list in a dictionary
pizza = { 
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# List of users with their favorite languages
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print (f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")