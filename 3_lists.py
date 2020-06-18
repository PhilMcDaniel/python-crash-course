#list ex
bikes = ['trek','giant','cannondale','redline']
print (bikes)

#print first value in list
print(bikes[0])
print(bikes[0].title())
print(bikes[1])
print(bikes[3])

#-1 position is last, -2 second from last
print(bikes[-1])
print(bikes[-2])

#formatted example
print(f"My first bike was a {bikes[0].title()}.")


#change value of first object in list
motos = ['honda','yamaha','suzuki']
print(motos[0])
motos[0]= 'ducati'
print(motos[0])

#append adds to end of list
motos = ['honda','yamaha','suzuki']
motos.append("ducati")
print (motos)

#can initialize empty list and add later
motos = []
print(motos)
motos.append('honda')
motos.append('yamaha')
motos.append('suzuki')
print(motos)

#insert() lets you add to list at location of your choosing
motos = ['honda','yamaha','suzuki']
motos.insert(0,'ducati')
print(motos)

#remove from list using del
del motos[0]
print (motos)

#pop removes from end of list, but can be accessed
pop_motos = motos.pop()
print(motos)
print(pop_motos)
#can pop from any position with index value passed
pop_motos = motos.pop(1)
print(pop_motos)

#removing based on value
motos = ['honda','yamaha','suzuki','ducati']
print(motos)
motos.remove('ducati')
print(motos)

#organizing a list
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.sort()
print(cars)
#reverse order, does not sort alphabetically
cars.sort(reverse=True)
print(cars)

#length of list
print(len(cars))