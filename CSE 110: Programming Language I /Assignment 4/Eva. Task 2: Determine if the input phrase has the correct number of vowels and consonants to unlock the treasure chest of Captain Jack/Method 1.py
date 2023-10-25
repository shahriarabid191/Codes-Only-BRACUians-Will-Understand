'''
Disclaimer:

The purpose of this publication is just to share a way of solving a problem. In no way, we claim this solution to be a perfect one. We firmly believe that 'Ideas give birth to more ideas'. We strongly encourage you to try to solve the problem on your own at first. You are recommended to refer to this publication only when you think you need some hints after giving multiple tries or when you want to explore if there are any other methods of solving the problem.
Lastly, apologies in advance in case of any error in the code or if the code is not understandable at all. You are requested to share any kind of feedback via the email address provided in the profile. Thank you.

N.B: We acknowledge the fact that you may find it challenging to understand the code in its raw form without any comments. Until we have added the comments, you may find it helpful to understand the code by taking help from AI tools like chatGPT.
'''





'''
Evaluation Task - 2:

Problem in brief:

Captain Jack and his crew have discovered a treasure chest full of gold coins. However, the chest comes with a mysterious lock. To open it, they need to input a phrase that should contain a combination of characters where vowel count is divisible by 3 and consonant count is divisible by 5. Write a Python program to help Captain Jack determine if the input phrase has the correct number of vowels and consonants to unlock the treasure chest.
Note: Vowels and Consonants count has to be greater than 0 for the treasure to open
'''





S = input()
vowelsList = "AEIOUaeiou"
    # can also be written as a list like this:
    # list_of_vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

vowel_count = 0
consonant_count = 0

for i in S:
    if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
        if i in vowelsList:
            vowel_count += 1
        else:
            consonant_count += 1

if (vowel_count > 0 and consonant_count > 0) and (vowel_count % 3 == 0 and consonant_count % 5 == 0):
    print("Aaarr! Me Plunder!!")
else:
    print("Blimey! No Plunder!!")
