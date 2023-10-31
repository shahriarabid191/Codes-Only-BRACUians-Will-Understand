'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





'''
Home Task - 2

Problem in brief:

Write a Python program that will take one input from the user made up of two strings separated by a comma and a space. Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string. 

[Do not use lists for this task]

Hint: For adding the leftover characters you may use string slicing.
'''





given_string = input()
new_string = ""

for i in range(len(given_string)):
  if given_string[i] == ",":
    first_part = given_string[:i] 
    second_part = given_string[i+2:]
    break

i = 0
j = 0 
while i < len(first_part) or j < len(second_part):
  if i < len(first_part):
    new_string += first_part[i]
    i += 1
  if j < len(second_part):
    new_string += second_part[j]
    j += 1

print(new_string)
