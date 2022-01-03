matrix = [[1,2,3], [4,5,6], [7,8,9]]

for row in matrix:
    for col in row:
        print(col)
        


numbers = [1,2,3,4,5,2,6,5,7,8]
# numbers.append(15)
# numbers.insert(2, 12)
# numbers.remove(1)
# numbers.pop()
# numbers.sort()
# print(numbers.index(5))
# print(numbers)
# print(numbers.count(5))
# numbers.clear()

list_of_numbers = []
for number in numbers:
    if number not in list_of_numbers:
        list_of_numbers.append(number) 
print(list_of_numbers)
        
        


