from typing import Counter


number = int(input('Enter a number: '))
counter = 2;
while counter <= number:
    divisor = 1
    sum_of_divisors = 0
    while divisor < counter:
        if counter % divisor == 0:
            sum_of_divisors += 1
        divisor += 1
    if counter == sum_of_divisors:
        print(counter,"is perfect")
    if counter < sum_of_divisors:
        print(counter,"is abundant")
    if counter > sum_of_divisors:
        print(counter,"is deficient")
    counter += 1
