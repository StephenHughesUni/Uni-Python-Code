# Stephen Hughes
# Jan 27 2021
# Tutorial Sol
# Q1
"""
LIMIT = 5.00
prices = []  # initializing list
from statistics import mean

# read in 5 prices into the loop
for i in range(5):  # Looping 5 times.
    users_price = float(input(f"Price: {i+1}: "))  # Asking user and making the print display 1 2 3 4 etc
    prices.append(users_price)  # Placing the users input INTO the list.

print(prices)  # Printing the output
print(f"Sum of the prices $ {sum(prices)}")

# Calculate average
average = mean(prices)
print("Average of price $" + str(round(average, 2)))

# display prices < 5.00
for item in prices:
    if item < LIMIT:
        print("Prices < $5.00: {:<6}".format(item))

# display prices higher than calculated average
print("{:15}{:10}".format("Price Number", "Value"))
for index, item in enumerate(prices):
    print("{:<15}{:<10}".format(index + 1, item))

# Q2
letters = ["a","b","c"]
for i in range(len(letters)):
    print(letters[i] + ", ")

a = [1.1, 2.2, 3.3]
print(a[0], " ", a[1], " ", a[2])
a[1] = a[2]
print(a[0], " ", a[1], " ", a[2])

# Q 3
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 10):
    print(i)
    sample[i] = 3 * i
print(sample)
"""
# Q4

scores = []  # Initialising empty list

# Populating empty list.
for i in range(5):  # Looping 5 times.
    scores.append(int(input(f"Enter scores: {i + 1}: ")))  # Append and Asking user
print(scores)
#  determine and score highest
max_score = max(scores)
print("Highest Score:", max_score)

for index, score in enumerate(scores):
    print("Score {:<3} :{:<4}differs from the max by {:<4}".format(index + 1, score, max_score - score))
