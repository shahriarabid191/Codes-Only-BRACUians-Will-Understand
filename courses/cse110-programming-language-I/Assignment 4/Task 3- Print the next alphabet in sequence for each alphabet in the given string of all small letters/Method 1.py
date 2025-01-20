'''
Home Task - 3

Problem in brief:

Write a Python program that takes a string as an input from the user containing all small letters and then prints the next alphabet in sequence for each alphabet in the input.

Hint: You may use the functions ord( ) and chr( ). The ASCII value of ‘a’ is 97 and ‘z’ is 122.
'''





given_string = input()
new_string = ""

for i in given_string:
  if i == "z":
    new_string += "a"
  else:
    new_string += chr(ord(i) + 1)
    
print(new_string)