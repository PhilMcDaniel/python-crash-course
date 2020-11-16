#input() has a single prompt parameter. Pauses execution and waits for input
message = input("Tell me something about yourself and I will tell it back to you")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}")

#multi-line prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, {name}")


#input response is always a string, until it isnt
age = input("How old are you? ")
print(age)
#This would throw an error
# age>21

#convert input to int
print(int(age)>21)