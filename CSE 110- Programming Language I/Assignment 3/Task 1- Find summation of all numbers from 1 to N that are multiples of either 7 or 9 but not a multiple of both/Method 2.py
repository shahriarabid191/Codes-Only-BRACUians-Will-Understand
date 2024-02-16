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