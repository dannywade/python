def print_models(unprinted, completed):
    """ Simulate printing each design, until none are left.
    Move each design to completed after printing. """
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}...")
        completed.append(current_design)

def show_completed(completed_models):
    """ Show all the completed models that were printed """
    print("\nThe following models were printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_models = ['phone case', 'robot', 'necklace']
completed_models = []

# Passing copy of list as argument
print_models(unprinted_models[:], completed_models)
show_completed(completed_models)

print(unprinted_models)