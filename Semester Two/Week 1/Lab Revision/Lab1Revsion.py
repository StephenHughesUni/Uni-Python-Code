"""
Question 1
Stephen Hughes - X00179579
Rainfall

# Lists
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week_days = []
total = 0
exceeding = 3.5

# Function
for i in range(7):
    rainfall = float(input(f" How much rainfall happened in CM on {days_of_the_week [i]}:"))
    total += rainfall
    week_days.append(rainfall)
    if rainfall > exceeding:
        print(f" There was an exceeding of 3.5cm on  {days_of_the_week [i]}.")
# Output
print(week_days)
print(f"The total of the week was: {total}cm")
average = total / len(week_days)
average = round(average, 2)
print(f"The average rainfall for the week is: {average}cm")
"""

"""
Question 2 
Stephen Hughes - X00179579
Add number to list
"""

# Lists declared
numberList = []
new_list = []

# Input
size = int(input("How big would you like the list: "))

# Function
for i in range(0, size):
    number = int(input(f"Enter the number {i+1} :"))
    numberList.append(number)
    new_list = [x + 1 for x in numberList]

# Output
print("User list is:", numberList)
print("The new list with +1 is", new_list)


"""
Question 3
Stephen Hughes - X00179579
Salespeople of company.

# Lists
salesPeople = []

# Input
size_of_people = int(input("Enter how many sales people to evaluate: "))

# Function
for i in range(0, size_of_people):
    sales = float(input(f"Enter sales amount of person {i+1}  : "))
    salesPeople.append(sales)

# Output
print("Total Sales: ", sum(salesPeople))
print("Average Sales: ", sum(salesPeople) / len(salesPeople))
print("Max Sales: ", max(salesPeople))
print("Min Sales: ", min(salesPeople))

"""