'''
Evaluation Task - 1

Problem in brief:

Write a program that takes a string as input and prints “Binary Number” if the string contains only 0s or 1s. Otherwise, print “Not a Binary Number”.
'''





x = input()
binary_digit = "01"
is_binary = 1

for i in x:
    if i not in binary_digit:
        is_binary = 0

if is_binary == 1:
    print("Binary Number")
else:
    print("Not a Binary Number")