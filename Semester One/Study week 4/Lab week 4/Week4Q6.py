# Stephen Hughes - X00179579
# 02/11/2020
# Week 4 Question 6
# Repeating a word without a blank space at the end.

user_word = input("Please enter a word you want to repeat: ")
user_amount = int(input("The number of times you want to have it repeated: "))


repeat = (user_word + " ") * (user_amount - 1) + user_word

print(repeat)
