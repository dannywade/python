size_input = input("What size are you? ")
text_input = input("What text would you like on the t-shirt? ")

def tshirt(size, text):
    """Docstring - function that collects t-shirt size and text"""
    print(f"Your size is {size}")
    print(f"Here's the text you wanted {text}")

tshirt(size=size_input, text=text_input)