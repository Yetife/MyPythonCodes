limit = int(input("Enter a number: "))
count = 1
sum = 0

while count <= limit:
    sum += count
    count = count + 1
print (count, sum)
average = sum / (count-1)
print("Average 0f sum of integers from 1 to", limit, "is", average)