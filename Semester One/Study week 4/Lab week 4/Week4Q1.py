# Stephen Hughes - X00179579
# 02/11/2020
# Week 4 Question 1
# This program is designed to take input from user in hours, minutes, seconds and then to output total seconds

SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 3600

hours = int(input("Please how many hours:"))
minutes = int(input("Please enter how many minutes"))
seconds = int(input("Please enter number of seconds"))

hours_in_seconds = hours * SECONDS_IN_HOUR
minutes_in_seconds = minutes * SECONDS_IN_MIN
total_overall = hours_in_seconds + minutes_in_seconds + seconds

print(hours, "hours", minutes, "minutes and", seconds, "seconds totaled is", total_overall, "seconds")
