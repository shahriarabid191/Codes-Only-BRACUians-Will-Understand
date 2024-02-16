'''
Problem in brief:

Given a string of fixed format containing food items and prices, create a program to calculate the bill.

Note: You are not allowed to use any built-in string manipulation functions except for len, chr, and ord. Also, there are no numerical characters present in the string except for the prices and they are represented as floating-point numbers.

Sample input: First item: 12.99$, Second item: 10.99$, Third item: 14.11$
'''





food_items = input()

total = 0.0

for i in range(len(food_items)):
    if food_items[i] == ":":
        colon_index = i
    if food_items[i] == "$":
        price = food_items[colon_index + 2:i]
        total += float(price)

print("The bill is: " + str(total) + "$")


#Credit: Showalihin Islam Fahim