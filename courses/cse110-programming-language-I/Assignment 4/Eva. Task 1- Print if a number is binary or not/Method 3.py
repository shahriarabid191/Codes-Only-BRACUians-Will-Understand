'''
Evaluation Task - 1

Problem in brief:

Write a program that takes a string as input and prints “Binary Number” if the string contains only 0s or 1s. Otherwise, print “Not a Binary Number”.
'''





x = input()

count = 0

for i in x:
    if i == "0" or i == "1":
        count += 1

if count == len(x):
    print("Binary Number")
else:
    print("Not a Binary Number")


#Credit: Showalihin Islam Fahim