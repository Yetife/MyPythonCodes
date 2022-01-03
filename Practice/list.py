days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
chars = ["a", "b", "c", "d", "e"]

print ("Day one is", days[1], "number [1:6]", numbers[1:6])
print ("Day two is", days[2])
days[2] = "January"
print ("Day two is", days[2])
del days[2];
print ("Day two is", days[2])

print (days.join(","))
