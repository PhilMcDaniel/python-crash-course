magicians = ['alice','david','carolina']
#print each entry in list
for magician in magicians:
	print(magician)

#for loop with formatted text
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone, that was a great show")



#numerical loops
#loop ends when max value is hit. Need to +1 to ensure 1-5 are all printed
for value in range(1,6):
	print(value)

numbers = list(range(1,6))
print (numbers)

#skip numbers, use third param in range()
even_numb = list(range(0,11,2))
print(even_numb)

#first 10 square numbers
square_numb = []
for num in range(1,11):
	num = num**2
	square_numb.append(num)
	#square_numb.append(num**2)
print(square_numb)

digits = [1,2,3,4,5,6,7,8,9,0]
min_d = min(digits)
print(min_d)
max_d = max(digits)
print(max_d)
sum_d = sum(digits)
print(sum_d)

#single line to create first 10 squares
squares = [value**2 for value in range(1,11)]
print(squares)


#slicing list
players = ['charles','martina','michael','florence','eli']
print (players[0:3])
print (players[1:4])
#start at beginning and give me 4
print (players[:4])
#start at two and give me rest of list
print(players[2:])
#last three in list
print(players[-3:])

#looping through a slice

print("Here are the first three players in my team:")
for player in players[:3]:
	print (player)

#copying lists
my_foods = ['pizza','ice cream','pasta','cake']
print(my_foods)
your_foods = my_foods[:]
print (your_foods)
my_foods.append('tacos')
your_foods.append('celery')
print(my_foods)
print(your_foods)


#tuples = immutable list. uses () instead of []
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#tuple with single value needs trailing comma
dimensions = (30,)
print(dimensions[0])

#loop over tuple
dimensions = (200,50,10,1,0,99)
for dimension in dimensions:
		print (dimension)
dimensions = (200,50,10)