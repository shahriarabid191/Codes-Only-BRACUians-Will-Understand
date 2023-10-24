'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





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
