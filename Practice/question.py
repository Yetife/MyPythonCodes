# import math

# name = input("What is your name? ")
# color = input("What is your favourite color? ")

# print(name + " likes " + color)

# # formatted String
# first = 'John'
# last = 'Smith'
# message = f'{first} [{last}] is a coder'
# print(message) 


weight = int(input('weight: '))
unit = input('(L)bs 0r (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')