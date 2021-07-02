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