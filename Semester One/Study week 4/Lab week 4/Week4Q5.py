# Stephen Hughes - X00179579
# 02/11/2020
# Week 4 Question 5
# Takes user input and creates a word from the first 2 and last 2 letters.

user_string = input("Enter a word that is longer than 4 letters :")

first2 = user_string[:2]
last2 = user_string[-2:]
print(first2 + last2)