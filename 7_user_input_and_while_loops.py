# input() has a single prompt parameter. Pauses execution and waits for input
message = input("Tell me something about yourself and I will tell it back to you")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}")

# multi-line prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, {name}")


# input response is always a string, until it isnt
age = input("How old are you? ")
print(age)
# This would throw an error
# age>21

# convert input to int
print(int(age) > 21)


height = input("How tall are you in inches? ")
height = int(height)

print(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("You'll be able to ride when you get taller")

# modulo = remainder of division num % denom
# when 0 returned, then the numbers are divisible
4 % 3
6 % 2

number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")

# while loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"

message = ""
while message != "quit":
    message = input(prompt)
    # This is added so that the word quit is not printed out when it is the message value from input
    if message != "quit":
        print(message)

# using a flag to accomplish the same thing
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)


# using break to exit

prompt = "\nEnter a city that you have visted:"
prompt += "\n(Enter 'quit' to finish.)"

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# using continue to go back to beginning of loop logic
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue
    print(current_number)


x = 1
while x <= 5:
    print(x)
    x+=1

#while loops with lists and dicts
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
#verify each user until all are confirmed
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#display confirmed users
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())


#removing specific values from list
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#filling a dictionary
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name:")
    response = input("Which mountaing would you like to climb? ")
    #store
    responses[name] = response
    repeat = input("Would you like to let another user respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")