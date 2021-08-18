with open('10_pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
#reading file like this ends up with extra blank string at end of file
print(contents.rstrip())

#read line by line
file_name = '10_pi_digits.txt'
with open(file_name) as file:
    for line in file:
        #need to strip newline characters stored at end of each line
        print(line.rstrip())

#read file into list of lines

with open(file_name) as file:
    lines = file.readlines()
print(lines)

for line in lines:
    print(line.rstrip())

#working with file contents
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
len(pi_string)

#large files (1 mil digits)
file_name = '10_pi_million_digits.txt'
with open(file_name) as file:
    lines = file.readlines()
print(lines)
pi_string=''
for line in lines:
    pi_string+=line.strip()
len(pi_string)

#first 50 chars
print(pi_string[:50])

#is your birthday containted in pi
birthday = input("enter your birthday, mmddyy: ")
if birthday in pi_string:
    print('your birthday appears in the first million digits of pi!')
else:
    print('sorry your birthday is not in the first million digits of pi')



#writing to an empty file
#2nd parm(r=read,w=write,append=a,r+=readwrite) read is the default
filename ='10_programming.txt'
with open(filename,'w') as file:
    file.write('I love programming')

#multiple lines
filename ='10_programming.txt'
with open(filename,'w') as file:
    #need to include \n or these will both be on the same line
    file.write('I love programming\n')
    file.write('I love creating new games\n')

#appending
with open(filename,'a') as file:
    file.write('I love finding meaning in large datasets\n')
    file.write('I love creating apps that can run in a browser\n')
    
#exceptions
print(5/0)
try:
    print(5/0)
#catching specific error for divide by 0
except ZeroDivisionError:
    print('you cant divide by zero')
#if try code works, except code does not run.

print('give me two numbers and Ill divide them')
print('enter q to quit')

while True:
    first_num = input('\nFirst number: ')
    if first_num == 'q':
        break
    second_num = input('Second number: ')
    if second_num =='q':
        break
    #try/catch for divide by zero
    try:
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print('you cant divide by zero!')
    #else runs with success of try block
    else:
        print(answer)

#handling FileNotFoundError exception
filename = 'alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'sorry the file {filename} not exist')

title = 'Alice In Wonderland'
title.split(' ')

#wordcount
filename = '10_alice.txt'
try:
    with open(filename,'r',encoding='utf-8') as f:
        contents = f.read()
except:
    print('file does not exist')
else:
    words = contents.split(" ")
    num_words = len(words)
    print(f"{filename} has around {num_words} words")

#working with multiple files
def count_words(filename):
    """count the approximate number of words in a file."""
    try:
        with open(filename,'r',encoding='utf-8') as f:
            contents = f.read()
    except:
        print('file does not exist')
    else:
        words = contents.split(" ")
        num_words = len(words)
        print(f"{filename} has around {num_words} words")

filename = '10_alice.txt'
count_words(filename)

filenames = ['10_alice.txt','10_siddhartha.txt','10_moby_dick.txt','10_little_women.txt']
for file in filenames:
    count_words(file)


#storing data
#json is a good option for storing data

import json
numbers = [2,3,5,7,11,13]

filename = '10_numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)

with open(filename,'r') as f:
    numbers=json.load(f)
print(numbers)

#saving and reading user-generated data
username = input('What is your name?')

#store data from input
filename = '10_username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"We'll remember you when you come back, {username}")

#load data that was stored
with open(filename) as f:
    username = json.load(f)
    print(f'welcome back, {username}')


#load stored data if exists, else prompt for value
filename = '10_username.json'
try:
    with open(filename,'r') as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('What is your name?')
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"we'll remember you when you comeback, {username}")

#refactor by puting in function

def greet_user():
    """greet the user by name"""
    filename = '10_username.json'
    try:
        with open(filename,'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('What is your name?')
        with open(filename,'w') as f:
            json.dump(username,f)
            print("we'll remember you when you come back, {username}")
    else:
        print(f'welcome back {username}')
greet_user()

def get_stored_username():
    """Get stored username, if available"""
    filename = '10_username.json'
    try:
        with open(filename,'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"welcome back {username}")
    else:
        username = input('Whats your name?')
        filename = '10_username.json'
        with open(filename,'w') as f:
            json.dump(filename,f)
            print(f"we'll remember you {username}")

greet_user()

#all pieces inside functions
def get_stored_username():
    """Get stored username, if available"""
    filename = '10_username.json'
    try:
        with open(filename,'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """prompt for a new username"""
    username = input("What is your name?")
    filename = '10_username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"welcome back {username}")
    else:
        username = get_new_username()
        print(f"we'll remember you when you come back {username}")
greet_user()