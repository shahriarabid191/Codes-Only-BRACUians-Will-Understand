'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





'''
Home Task - 1

Problem in brief:

Write a Python code for the following:
Ask the user to enter a Number, N.
From 1 to N (inclusive), display the summation of all numbers that are multiples of either 7 or 9 but not a multiple of both.    
'''





N = int (input())
sum = 0
for i in range (1, N + 1, 1):
  if (i % 7 == 0 and i % 9 != 0) or (i % 7 != 0 and i % 9 == 0):
    sum += i
print(sum)


#Credit: Showalihin Islam Fahim
