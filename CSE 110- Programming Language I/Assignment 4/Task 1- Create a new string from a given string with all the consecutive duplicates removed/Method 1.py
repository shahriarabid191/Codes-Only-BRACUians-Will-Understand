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