# Stephen Hughes
# 15/02/2021
# X00179579

# Maths Import
from statistics import mean

# Lists and then all appended
grade1 = [10.5, 12.0, 14.5, 16.75, 18.0]
grade2 = [20.5, 22.25, 24.0, 26.25, 28.0]
grade3 = [34.0, 36.5, 38.0, 40.35, 43.0]
grade4 = [50.0, 60.0, 70.0, 80.0, 99.99]
grades = [grade1, grade2, grade3, grade4]

# Formatting the heading
print("-" * 110)
print("{0:>25}{1:>20}{2:>20}{3:>20}{4:>20}".format("Step 1", "Step 2", "Step 3", "Step 4", "Step 5"))
print("-" * 110)
# setting a loop to go through each list in grades to print format out
for i, row in enumerate(grades):
    print("{0:<20}".format("Grade :" + str(i + 1)), end="")
    for col in row:
        print("{0:<20}".format(col), end="")
    print()
print("-" * 110)
print()

# Calculating Average by getting the mean function of grades [2] which is grade 3 as index starts from 0
# Q1
average3 = mean(grades[2])
print(f"The average of Grade 3 is {average3}")
print()
print("-" * 110)

# Looping through grades and finding using mean for each grade list
# Q2
for index, grade in enumerate(grades):
    average = mean(grade)
    print(f"The average of grade {index + 1} is {average}")

# Looping through grades again instead of mean finding the difference with min and max of each grade
# Q3
print("-" * 110)
for index, grade in enumerate(grades):
    Mingrade = min(grade)
    Maxgrade = max(grade)
    difference = Maxgrade - Mingrade
    print(f"The difference between grades in grade {index + 1} is {difference}")

# Formatting heading for the +1.5 same as above
print("-" * 110)
print("{0:>25}{1:>20}{2:>20}{3:>20}{4:>20}".format("Step 1", "Step 2", "Step 3", "Step 4", "Step 5"))
print("-" * 110)

# Same as before but adding the format listname[rowno][colno] = new value of 1.5
for i, row in enumerate(grades):
    print("{0:<20}".format("Grade :" + str(i + 1)), end="")
    for colid, col in enumerate(row):
        grades[i][colid] += 1.5
        print("{0:<20}".format(grades[i][colid]), end="")
    print()
print("-" * 110)
print(grades)
#  format- list_name[row_no][col_no] = new_value
