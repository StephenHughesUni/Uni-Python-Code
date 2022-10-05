"""
def display_pi():
    PI = (22.0 / 7.0)
    print(f"Pi = {PI}")

for i in range(5):
    display_pi()


import time
def display_time():
    time_now = time.strftime("%H:%M:%S")
    print(time_now)

for i in range(5):
    display_time()



# SH
# X00179579
# Q1

with open("read it.txt", "r") as file:
    contents = file.read()

print("Conents are:")
print(contents)



# Q2

list_of_lines = []
with open("read it.txt", "r") as input_file:
    for num in range(5):
        list_of_lines.append(input_file.readline().rstrip())

print(list_of_lines)



# Q3
with open("output.txt", "a") as output_file:  # a or w will create the file but w will override contents while a will
    # append to end
    output_file.write("Python File Exercisesv2\n")
    output_file.write("Java Exercisesv2\n")

with open("output.txt", "r") as input_file:
    print(input_file.read())

# Q4

with open("read it.txt", "r") as input_file:
    lines = input_file.readlines()

print(lines)


# Q5

text_file = open("read it.txt", "r")

text = text_file.read()
text_file.close()

all_words = text.split()
print(all_words)

print()
# or do below as with will automatically close
print()

with open("read it.txt", "r") as input_file:
    contents = input_file.read()
print(contents)
contents_list = contents.split()
print(contents_list)
print("Number of words:", len(contents_list))



# Q6
with open("read it.txt", "r") as input_file:
    contents = input_file.readlines()
print("Number of lines in readit.txt:", len(contents))


# Q7
colors = ["Red", "Green", "Blue", "White"]
with open("color.txt", "w") as color_file:  # a or w will create the file but w will override contents while a will
    for item in colors:
        color_file.write(item + "\n")

with open("color.txt", "r") as input_file:
    print(input_file.read())



# Q8

with open("read it.txt", "r") as main_file:
    contents = main_file.read()
print(contents)

# write contents to new file
with open("read it 2.txt", "w") as sub_file:
    sub_file.write(contents)
"""

# Q9
import random
with open("read it.txt", "r") as input_file:
    lists = input_file.readlines()
print("The lines are :", lists)
print("A random item from this list is :", random.choice(lists))
