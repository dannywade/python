responses = {}

#Setting a flag
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb?")

    #Store the response in the dictionary
    responses[name] = response

    #Find out if anyone else wants to take the survey
    repeat = input("Does anyone else want to take the survey?")
    if repeat == 'no':
        polling_active = False
    
# Polling complete. Show results
print("\n--- Polling results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")