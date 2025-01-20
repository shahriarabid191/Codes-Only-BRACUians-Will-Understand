'''
Home Task - 2:

Problem in brief:

Write a Python program that takes a number from the user and prints its digits from left to right.
[Consider the input number to be an INTEGER. You are not allowed to use String indexing for solving this task]
'''





i = int(input())
temp = i

count = 0
while temp != 0:
    count += 1
    temp //= 10

y = 10 ** (count - 1)
while i != 0:
    if i < 10:
        print(i // y, end="")
    else:
        print(i // y, end=", ")
    i %= y
    y //= 10