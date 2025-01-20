'''
Home Task - 4:

Problem in brief:

Write a Python program that asks the user for a quantity, then takes that many numbers as input and prints the maximum, minimum and average of those numbers.
[Please note that you CANNOT use max, min built-in functions]
[Also, you DO NOT need to use lists for this task]
'''





n = int(input())
numberOfInputs = n

max = int(input())
min = int(input())

if max < min:
    temp = max
    max = min
    min = temp

sum = max + min

while n > 2:
    y = int(input())
    sum += y
    if y > max:
        max = y
    elif y < min:
        min = y
    n -= 1

print("Maximum", max)
print("Minimum", min)
print("Average is", (sum / numberOfInputs))