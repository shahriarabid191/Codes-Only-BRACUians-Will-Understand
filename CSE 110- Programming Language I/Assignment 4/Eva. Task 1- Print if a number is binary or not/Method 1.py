'''
Evaluation Task - 1

Problem in brief:

Write a program that takes a string as input and prints “Binary Number” if the string contains only 0s or 1s. Otherwise, print “Not a Binary Number”.
'''





x = input()
is_binary = True

for i in x:
    if i != "0" and i != "1":
        is_binary = False
        break

if is_binary:
    print("Binary Number")
else:
    print("Not a Binary Number")