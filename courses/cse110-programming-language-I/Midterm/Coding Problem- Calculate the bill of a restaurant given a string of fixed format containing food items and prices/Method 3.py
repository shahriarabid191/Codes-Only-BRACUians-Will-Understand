'''
Problem in brief:

Given a string of fixed format containing food items and prices, create a program to calculate the bill.

Note: You are not allowed to use any built-in string manipulation functions except for len, chr, and ord. Also, there are no numerical characters present in the string except for the prices and they are represented as floating-point numbers.

Sample input: First item: 12.99$, Second item: 10.99$, Third item: 14.11$
'''







food_items = input()
total = 0.0
price = ""

for i in food_items:
    if ord("0") <= ord(i) <= ord("9") or i == ".":
        price += i
    if i == "$":
        total += float(price)
        price = ""

print(f"The bill is: {total}$")


#Credit: Azmayen Aziz