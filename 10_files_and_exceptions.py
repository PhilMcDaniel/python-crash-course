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