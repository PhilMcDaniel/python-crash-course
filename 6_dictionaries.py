#dictionary is group of key-value pairs

alien_0 = {'color':'green','points':'5'}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points.")


#adding values to dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)


#start with empty dictionary
alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#change value

print(alien_0['color'])
alien_0['color'] = 'yellow'
print(alien_0['color'])

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(alien_0)

#move to right
#alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#removing values

print(alien_0)
del alien_0['speed']
print(alien_0)


fav_lang = {
    'jen':'python'
    ,'sarah':'c'
    ,'edward':'ruby'
    ,'phil':'python'
    }
print(fav_lang)

lang = fav_lang['sarah'].title()
print(f"Sarah's favorite language is {lang}")

#using get() to provide defaults
alien_0 = {'color':'green','speed':'slow'}
# The below fails because that key does not exist
# print(alien_0['points']
print(alien_0.get('points','No points value assigned'))


#looping through dictionary
user_0 = {
    'username':'efermi'
    ,'first':'enrico'
    ,'last':'fermi'
}
print(user_0)

for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

fav_lang = {
    'jen':'python'
    ,'sarah':'c'
    ,'edward':'ruby'
    ,'phil':'python'
    }
for name,language in fav_lang.items():
    print(f"{name.title()}'s favorite language is {language}.")

#loop through only keys (use keys() method)
for name in fav_lang.keys():
    print(name.title())

friends = ['phil','sarah']
for name in fav_lang.keys():
        print(f"Hi, {name.title()}.")

        if name in friends:
            language = fav_lang[name].title()
            print(f"\t{name.title()}, I see you love {language}")
if 'erin' not in fav_lang.keys():
    print("Erin, please take our poll")

#looping through dictionary in a specific order
fav_lang = {
    'jen':'python'
    ,'sarah':'c'
    ,'edward':'ruby'
    ,'phil':'python'
    }
for name in sorted(fav_lang.keys()):
        print(f"{name.title()}, thank you for taking our poll!")

print("The following languages have been mentioned:")
for lang in fav_lang.values():
    print({lang.title()})

#using set() to de-dupe
#"python" was listed twice
for lang in set(fav_lang.values()):
    print({lang.title()})


#nesting
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#using loop to create multiple dictionary values
aliens=[]

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#display first 5
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")

#modify 3 rows to change a value
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")

#list in dictionary

pizza={
    'crust':'thick'
    ,'toppings':['mushroom','extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza"
" with the following toppings:")
for topping in pizza['toppings']:
    print(topping)


fav_lang = {
    'jen':['python','ruby']
    ,'sarah':['c']
    ,'edward':['ruby','go']
    ,'phil':['python','haskell']
    }

for name,lang in fav_lang.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for lang in lang:
        print(f"\t{lang.title()}")

#dictionary in a dictionary
users = {
    'aeinstein': {
        'first':'albert'
        ,'last':'einsein'
        ,'location':'princeton'
    }
    ,'mcurie': {
        'first':'marie'
        ,'last':'curie'
        ,'location':'paris'
    }
}
for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")