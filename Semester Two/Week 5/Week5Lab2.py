# Stephen Hughes
# X00179579
# 22 / 02 / 2021

# Q1
import csv
total = 0
count = 0
average = 0
with open("pima.csv", "r", newline='') as file:
    my2DListOfPima = list(csv.reader(file))
    for i, info in enumerate(my2DListOfPima):
        if info[2] != '0':
            total += int(info[2])
            count += 1
        else:
            pass
    average = total // count
    print(my2DListOfPima)
    print("The total of Pima is", total)
    print("The average of Pima is", average)
    file.close()

with open('pimaNew.csv', 'w', newline="") as newPima:
        writer = csv.writer(newPima)
        for i, info in enumerate(my2DListOfPima):
            if info[2] == '0':
                info[2] = average
            writer.writerow(info)

# Q2
def random_num_gen():
    import random

    print(random.randint(0,100))

for i in range(10):
    random_num_gen()

# Q3
def zerotolimit(limit_in):
    for num in range(0, limit):
        if num % 2 != 0:
            print(num, end = " ")
limit = int(input("please enter limit: "))
zerotolimit(limit)

# Q4
def largest_string(string1_in, string2_in):
    if len(string1) > len(string2):
        print("The string", string1, "is larger")
    elif len(string1) < len(string2):
        print("The string", string2, "is larger")
    else:
        print("The two strings are equal")

string1 = input("Please enter first string:")
string2 = input("Please enter second second:")
largest_string(string1, string2)