#simple example

def greet_user():
    #docstring for automating documentation. Triple quotes
    """Display a simple greeting."""
    print("Hello!")
greet_user()

#pass information to function

def greet_user(username):
    #docstring for automating documentation. Triple quotes
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")
greet_user('Bob')

#positional arguments
def describe_pet(animal_type,pet_name):
    """Diplay information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','harry')
describe_pet('dog','doge')
#this example shows that order of arugments matters
describe_pet('harry','hamster')
#this example shows the explicit use 
describe_pet(animal_type='hamster',pet_name='harold')
describe_pet(pet_name='doge',animal_type='dogo')

#default values
def describe_pet(pet_name,animal_type='dog'):
    """Diplay information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet('Max')
describe_pet(pet_name='peter',animal_type='plant')

#avoiding argument errors
def describe_pet(pet_name,animal_type):
    """Diplay information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet()

#returning simple value
def get_formatted_name(first,last):
    """Return a full name, neatly formatted."""
    full_name = f"{first} {last}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#optional argument
def get_formatted_name(first,last,middle=''):
    """Return a full name, neatly formatted."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
musician = get_formatted_name('john','hooker','lee')
print(musician)
musician = get_formatted_name('jimi','hendrix')
print(musician)


#returning dictionary
def build_person(first_name,last_name,age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix')
print(musician)
musician = build_person('jimi','hendrix',age=27)
print(musician)

#using function with while loop
def get_formatted_name(first,last,middle=''):
    """Return a full name, neatly formatted."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

while True:
    print(f"\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name =='q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}")


#passing a list

def greet_users(names):
    """print a simple greeting to each user in a list"""
    for name in names:
        msg = f"Hello {name.title()}"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

#modifying a list using a function
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

def print_models(unprinted_designs,completed_models):
    """
    Simulate printing each design until none are left.
    Move to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed"""
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#preventing a function from modifying a list
#[:] makes a copy of the list to send to the function
funtion_name(list_name[:])

print_models(unprinted_designs[:],completed_models)

#passing arbitrary number of arguments to function
#* is the keyword
def make_pizza(*toppings):
    """Summarize what we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('sausage','cheese','mushroom','greenpeppers')

#mixing positional and arbitrary number of args
def make_pizza(size,*toppings):
    """Summarize what we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'sausage','cheese','mushroom','greenpeppers')


#arbitrary keyword arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
#result is a tuple
make_pizza('pepperoni')
make_pizza('sausage','cheese','mushroom','greenpeppers')

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('sausage','cheese','mushroom','greenpeppers')

#mixing positional and arbitrary
# arbitrary needs to be last param
# often see *args as generic name for arbitrary positional arguments
def make_pizza(size,*toppings):
    """summarize the pizza"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f" - {topping}")

make_pizza(12,'pepperoni')
make_pizza(16,'pepperoni','cheese','green pep')


#using arbitrary keyword arguments
#**kwargs used for non-specific keyword arguments
# double asterisk causes python to create empty dict and fill with arguments passed
def build_profile(first,last, **user_info):
    """Build a dict containing everything we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)


#storing functions in modules
#module_name.function_name()
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(16,'mushrooms','green peppers','extra cheese')

#import specific function
#from module_name import function_name
#from module_name import function_name_0,function_name_1,function_name2

#use "as" to alias function
#from module_name import function_name as fn
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(16,'mushrooms','green peppers','extra cheese')

#us "as" to alias module
#import module_name as mn
import pizza as p

#import all functions ni a module
from pizza import *
#from module_name import *

#styling functions
#functions should have descriptive names
#add comment to explain what the function does
#don't use space when assigning default values
