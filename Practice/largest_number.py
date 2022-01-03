numbers = [10, 5, 30, 12, 13, 24, 15]

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)    