'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





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
    price = ""
    i += 2
    while food_items[i] != "$":
      price += food_items[i]
      i += 1
    total += float(price) 

print("The bill is: " + str(total) + "$")
