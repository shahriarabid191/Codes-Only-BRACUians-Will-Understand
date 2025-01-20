'''
Home Task - 3:

Problem in brief:

Write a Python program that asks the user for an integer number and tells if it is a prime number or a perfect number or neither.
Note: A number cannot be both prime and perfect.
Prime Number: If a number has only two divisors, (1 and itself), then it is a prime number.
Perfect Number: A number is said to be a perfect number if the sum of its divisors, including 1 but not the number itself is equal to that number.
'''





y = int(input())

is_prime = True
for i in range(2, y, 1):
    if y % i == 0:
        is_prime = False
        break

sum = 0
for i in range(1, y, 1):
    if y % i == 0:
        sum += i

if sum == y:
    print(y, "is a perfect number")
elif is_prime:
    print(y, "is a prime number")
else:
    print(y, "is not a prime or perfect number")