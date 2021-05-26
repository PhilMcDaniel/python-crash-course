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