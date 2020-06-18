#simple print with var
message = "hello world!"
print(message)

#print same after changing var
message = "hola globa"
print(message)

#string manip and formatting
name = "john dOe"
print(name.title())
print(name.upper())
print(name.lower())


first_name = "john"
last_name = "doe"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")
print("\tPython")
print("Python\n\tPythonLine2")

langs = ' python '
print(langs)
print(langs.rstrip())
print(langs.lstrip())
print(langs.strip())

#integer/decimal stuff
print(3+2)
print(3/2)
print(3-2)

print(3**2)
print(2+3*4)
print((2+3)*4)

print(.2+.22)
large_num = 10_000_000
print(large_num)

x,y,z = 1,2,3
print(f"x={x} y={y} z={z}")

#constant in caps
CONSTANT = 333
print (CONSTANT)