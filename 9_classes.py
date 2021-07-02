#capital for classes
#function inside a class is called a method
#class is set of instructions to call a specific instance
class Dog:
    """A simple attempt to model a dog"""
    
    #__init__ is special method that python runs automatically when we create new instance of class
    #self is needed and must come first
    def __init__(self,name,age):
        """initialize name and age attributes"""
        #any variable with self. is available to entire class and any instance
        #variables that are accessable through instances are called attributes
        self.name = name
        self.age = age
    
    def sit(self):
        """simulate dog sitting after command"""
        print(f"{self.name} is now sitting")


    def roll_over(self):
        """simulate rolling over after command"""
        print(f"{self.name} rolled over!")

#instance of Dog class
#instance.attribute for accessing values of attributes
my_dog = Dog('willie',6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

#call a method from the instance of Dog my_dog
my_dog.sit()
my_dog.roll_over()

#creating multing instances
my_dog = Dog('willie',6)
your_dog = Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")


#Working with classes and instances
class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_car = Car('toyota','camry','2015')
print(my_car.get_descriptive_name())

#setting default value for an attribute
class Car:
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing car mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_car = Car('toyota','camry','2015')
print(my_car.get_descriptive_name())
my_car.read_odometer()

#modifying attribute values

#direct modification
my_car.odometer_reading = 23
my_car.read_odometer()

#modify via method
class Car:
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing car mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer to given value.
        Reject if there is an attempt to decrease"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage    
        else:
            print("You can't roll back the odometer")
        

my_car = Car('toyota','camry','2015')
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(24)
my_car.read_odometer()
my_car.update_odometer(10)


#incrementing an attribute via method
class Car:
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing car mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer to given value.
        Reject if there is an attempt to decrease"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage    
        else:
            print("You can't roll back the odometer")

    def increment_odometer(self,miles):
        """add given amount to odometer reading"""
        self.odometer_reading += miles

my_car = Car('toyota','camry','2015')
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(1500)
my_car.read_odometer()
my_car.increment_odometer(200)
my_car.read_odometer()


#inheritance
#when a class inherits from another, it takes the attributes and methods from the parent class. can define new attributes or methods

class Car:
    """Simple representation of a car"""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing car mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer to given value.
        Reject if there is an attempt to decrease"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage    
        else:
            print("You can't roll back the odometer")

    def increment_odometer(self,miles):
        """add given amount to odometer reading"""
        self.odometer_reading += miles

#inherited class
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric cars"""

    def __init__(self,make,model,year):
        """initialize attributes from parent"""
        #super() function reaches to parent class
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())


#extend child class with new method and attributes
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric cars"""

    def __init__(self,make,model,year):
        """initialize attributes from parent"""
        #super() function reaches to parent class
        super().__init__(make,model,year)
        self.battery_size = 75

    def describe_battery_size(self):
        """print a statement describing the battery"""
        print(f"The battery size is {self.battery_size}")

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery_size()


#override method from parent class
# define method in child class with same name as in parent class
class ElectricCar(Car):
    #assume the "Car" class had a method for this and we wanted to override it for ElectricCar    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")


#instances as attributes
#useful for breaking large classes into smaller ones that work together
class Battery:
    """simple model of battery for an electric car"""

    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery"""
        print(f"This car's battery size is: {self.battery_size}")

    def get_range(self):
        """print a statement about the battery's range"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles")

my_battery = Battery()
my_battery.describe_battery()

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric cars"""

    def __init__(self,make,model,year):
        """initialize attributes from parent"""
        super().__init__(make,model,year)
        
        #reference the battery class and create new attribute for child class
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#importing classes
#from file/module import class as alias