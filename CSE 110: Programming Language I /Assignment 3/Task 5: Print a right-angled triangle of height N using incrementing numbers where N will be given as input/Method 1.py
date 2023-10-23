'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.
'''





'''
Home Task - 5:

Problem in brief:

Write a python program that prints a right-angled triangle of height N using incrementing numbers where N will be given as input.
'''





N = int(input())
for x in range(1, N + 1, 1):
    for y in range(1, x + 1, 1):
        print(y, end="")
    print()
