'''
Home Task - 2:

Problem in brief:

Write a Python program that takes a number from the user and prints its digits from left to right.
[Consider the input number to be an INTEGER. You are not allowed to use String indexing for solving this task]
'''





# Same as method 1. Only the process of counting the number of digits in the given number is different.

number = int(input())

y = 10 ** (len(str(number)) - 1)

number = int(number)
while number != 0:
    if number < 10:
        print(number // y, end="")
    else:
        print(number // y, end=", ")
    number %= y
    y //= 10


#Credit: Abdullah Mazid Zomader