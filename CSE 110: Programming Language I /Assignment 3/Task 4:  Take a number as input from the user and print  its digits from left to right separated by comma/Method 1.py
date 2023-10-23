'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.
'''





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
