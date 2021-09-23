number = input("Number: ")
sum = 0

while number != 0:
    number = int(number)
    if number%2 == 1: 
        print ("Error, enter only even number")
        number = input("Number: ")
        continue
    sum += number
    number = input("Number: ")
print ("The sum is: " + sum)