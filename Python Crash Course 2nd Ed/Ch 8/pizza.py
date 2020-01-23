# Example of *args - creates empty tuple for arguments used

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')