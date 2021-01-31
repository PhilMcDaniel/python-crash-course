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