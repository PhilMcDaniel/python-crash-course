cars = ["audi","bmw","subaru","toyota"]
print(cars)

for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())
#set value
car = 'bmw'
#compare value
car =='bmw'
print(car == 'bmw')

#equality check is case-sensitive
car = 'Audi'
print(car =='audi')


toppings = "mushrooms"
print(toppings)
if toppings != "anchovies":
	print("hold the anchovies")
else:
	print ("bring on the anchovies")

#numerical comparisons
age = 18
print(age == 18)

answer = 25
if answer != 42:
	print("the answer is incorrect")

age = 19
print (age <= 21)
print (age > 21)

#multiple conditions w/ and
age_0 = 22
age_1 = 18
print (age_0 >= 21 and age_1 >= 21)
age_1 = 23
print (age_0 >= 21 and age_1 >= 21)

#multiple conditions w/ or
age_0 = 22
age_1 = 18
print (age_0 >= 21 or age_1 >= 21)

age_0 = 18
age_1 = 18
print (age_0 >= 21 or age_1 >= 21)

#checking values in a list
toppings = ['mushrooms','onions','pineapple']
print ('mushrooms' in toppings)
print ('pepperoni' in toppings)

#checking value not in a list
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
	print (f"{user.title()}, you are allowed to post a response")

#boolean
game_active = True
can_edit = False

#multiple actions
age = 19
if age >=18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")

#if else
age = 17
if age >= 18:
	print("You are old enough to vote yet")
else:
	print("Sorry, you are too young to vote")


#if elif else
age = 12
if age < 4:
	print("Your admission cost is $0")
elif age < 18:
	print("Your admission cost is $25")
else:
	print("Your admission cost is $40")


age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"Your admission cost is ${price}.")


#testing multiple conditions
toppings = ["mushrooms","extra cheese"]

#not using if elif because it would short circuit on single hit
if "mushrooms" in toppings:
	print("Adding mushrooms")
if 'pepperoni' in toppings:
	print("Adding pepperoni")
if 'extra cheese' in toppings:
	print("adding extra cheese")
print("\nFinished making your pizza")


#if/else with loop
toppings = ['mushrooms','green peppers','extra cheese']
#print(toppings)
for topping in toppings:
	if topping == 'green peppers':
		print("sorry, we are out of green peppers")
	else:
		print(f"adding {topping}.")
print("\nFinished making your pizza")

#checking for non empty list

toppings = []
if toppings:
	for topping in toppings:
		print(f"adding {topping}")
else:
	print("are you sure you want a plain pizza?")

a_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
r_toppings = ["mushrooms","french fries","extra cheese"]

for r_topping in r_toppings:
	if r_topping in a_toppings:
		print(f"adding {r_topping}")
	else:
		print(f"Sorry, we don't have {r_topping}")
print("\nFinished making your pizza")