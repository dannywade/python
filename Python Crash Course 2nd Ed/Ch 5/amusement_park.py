#Admission fees
#4 or under is free
#Between 4-18 is $25
#18 and older is $40

age = 12

if age < 4:
   price = 0
elif age > 4 and age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")
#Is more efficient since you only need to change one print statement