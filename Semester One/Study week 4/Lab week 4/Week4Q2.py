# Stephen Hughes - X00179579
# 02/11/2020
# Week 4 Question 2
# Calculates input radius from user.

PI = 3.14159
radius = float(input("Please enter radius :"))
area = radius * radius * PI
circumference = 2 * PI * radius
area = round(area, 3)
print("The area is " +str(area))
print("The circumference is "+str(circumference))