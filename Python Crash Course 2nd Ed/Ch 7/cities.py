prompt = "\nPlease enter a name of the city you visited."
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to visit the city {city.title()}")