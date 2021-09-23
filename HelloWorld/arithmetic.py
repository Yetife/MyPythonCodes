number_str = input("Enter a number")
number_int = int(number_str)
addition = number_int + 2
multiplication = addition * 3
subtraction = multiplication - 6
division = subtraction / 3
print("addition = ",addition,"\n multiplication = ", 
multiplication, "\n subtraction = ", subtraction, "\n division = ", division)

my_var1 = 7.0
my_var2 = 5
print(my_var1 % my_var2)

x = 4
y = 5
print(x//y)

var = 30 - 3 ** 2 + 8 // 3 ** 2 * 10
print(var)

userInput = input("Enter a number")
userInput_str = str(userInput)
userInput_int = int(userInput_str)
userInput_float = float(userInput_int)
print(userInput_str, userInput_int, userInput_float)

number_str = input("Enter a number")
number_int = int(number_str)
if number_int % 2 == 0:
    print('0')
elif number_int % 2 == 1:
    print('1')

time_str = input("Enter a time in seconds")
time_int = int(time_str)
hours = int(time_int / 60 /60)
minutes = int(time_int / 60)
seconds = int(time_int % 60)
print(hours,"hours,",minutes,"minutes", "and", seconds, "seconds")