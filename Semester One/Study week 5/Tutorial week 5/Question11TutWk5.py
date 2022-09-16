# Stephen Hughes
# Tutorial Solutions
# Question 11 Week 5

# constants
LIMIT = 5000.00
LOWER = 500.00

# inputs
cost = float(input("Cost of item: $"))

# processing
if cost > LIMIT:
    print("Go to tender")
elif cost >= LOWER:         # trapping values between 500 and 5000
    print("Get three quotes")
else:
    print("Order item")
