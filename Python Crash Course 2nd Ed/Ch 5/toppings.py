requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)


for item in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers")
    else:
        print(f"Adding {item}.")

print("\nFinished making your pizza.")



#Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested = ['mushrooms', 'fries', 'extra cheese']

for item in requested:
    if item in available_toppings:
        print(f"adding {item}.")
    else:
        print(f"Sorry, we don't have {item}")

print("Finished your pizza.")