'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





'''
Home Task - 1

Problem in brief:

Given a string, create a new string with all the consecutive duplicates removed. 

Note: Only consecutive letters are removed, not all duplicate occurrences of a letter.
'''





given_string = input()
new_string = ""

for i in range(0, len(given_string), 1):
    if i == 0 or given_string[i] != given_string[i - 1]:
        new_string += given_string[i]

print(new_string)
