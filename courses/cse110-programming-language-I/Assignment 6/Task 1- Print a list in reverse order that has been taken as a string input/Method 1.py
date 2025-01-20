'''
Task 1

Problem in brief:

Take a list of 5 elements as user input and print the list in reverse order. Slicing can be used handling the given list as input. But to reverse the list you must not use slicing and split( ).
Hint: You may use a loop to show the reversed list as a new list.
'''





inputString = input()
newList = []
reversedList = []

start = 1

for i in range(1, len(inputString)):
    if inputString[i] == "," or inputString[i] == "]":
        newList += [inputString[start : i]]
        start = i + 2

for j in range(len(newList) - 1, -1, -1):
    reversedList += [newList[j]]

print(reversedList)