'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.
'''





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
