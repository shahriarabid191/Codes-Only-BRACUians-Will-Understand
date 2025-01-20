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