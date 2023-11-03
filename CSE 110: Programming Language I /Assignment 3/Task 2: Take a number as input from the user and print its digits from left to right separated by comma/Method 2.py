'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





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
