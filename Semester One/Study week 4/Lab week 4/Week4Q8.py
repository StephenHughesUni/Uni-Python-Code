# Stephen Hughes - X00179579
# 02/11/2020
# Week 4 Question 8
# convert seconds from user input into hours , min , seconds - using mod "%" and floor div "//"

seconds = int(input("Please enter amount of seconds"))
minutes = seconds // 60
hours = minutes // 60

print ("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))