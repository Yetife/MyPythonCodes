top_num = int(input())
number = 2
while number <= top_num:
    divisor = 1
    sum_of_divisors = 0
    while divisor <= number:
        if number % divisor == 0:
            sum_of_divisors =sum_of_divisors + divisor
        divisor += 1
        if number == sum_of_divisors:
            print(number,"is perfect")
        if number < sum_of_divisors:
            print(number,"is abundant")
        if number > sum_of_divisors:
            print(number,"is deficient")
        number = number + 1
