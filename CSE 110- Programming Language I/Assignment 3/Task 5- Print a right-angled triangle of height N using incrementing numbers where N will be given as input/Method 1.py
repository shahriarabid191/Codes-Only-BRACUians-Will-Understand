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