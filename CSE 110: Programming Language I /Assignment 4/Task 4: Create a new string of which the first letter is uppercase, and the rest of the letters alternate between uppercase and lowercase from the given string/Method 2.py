'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





'''
Home Task - 4

Problem in brief:

Write a python program that takes a string as an input from the user and then modifies the string in such a way that the string always starts with an uppercase letter and the case of each subsequent letter is the opposite of the previous letter (uppercase character followed by a lowercase character followed by an uppercase character and so on). Finally, the modified string is printed to show the user.

Hint: Flags/counters can be used to manage uppercase-lowercase
'''





# Without .upper and .lower function. 
# Long variable names were used to increase readability.

given_string = input()
new_string = ""

is_capital = False

for i in range(len(given_string)):
  if (65 <= ord(given_string[i]) <= 90) or (97 <= ord(given_string[i]) <= 122):
    if is_capital:
      if 65 <= ord(given_string[i]) <= 90:
        new_string += chr(ord(given_string[i]) + 32)
      else:
        new_string += given_string[i]
      is_capital = False
    else:
      if 97 <= ord(given_string[i]) <= 122:
        new_string += chr(ord(given_string[i]) - 32)
      else:
        new_string += given_string[i]
      is_capital = True
  else:
    new_string += given_string[i]

print(new_string)
