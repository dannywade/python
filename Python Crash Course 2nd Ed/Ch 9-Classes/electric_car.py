"""Import multiple classes from one module"""

class Car:
    """A simple class to represent a class"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        #Default attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Prints the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    # Updating the odometer via method
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempt to roll back the odometer
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    # Incrementing the odometer via method (add miles to odometer_reading attribute)
    def increment_odometer(self, miles):
        self.odometer_reading += miles

"""
my_new_car = Car('audi', 'a4', 2020)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
"""

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)

        self.battery = Battery()
 

class Battery:
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car has a range of {range} miles on a full charge.")



"""
my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
"""