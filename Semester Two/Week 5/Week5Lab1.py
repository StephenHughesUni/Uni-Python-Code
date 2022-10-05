# Stephen Hughes
# X00179579
# 22 / 02 / 2021
# Q1

list_of_names = []
# For loop of information and appending it to list of names
for names in range(5):
    person_name = input("Please enter the name:")
    while len(person_name) < 10:
        person_name = input("Please enter name with 10 characters:")
    list_of_names.append(person_name)
# Opening text and writing the items inside of list of names on a new line to names.txt
with open("names.txt", "w") as input_file:
    for item in list_of_names:
        input_file.write(item + "\n")
# Visual print of the reading of input file
print("-" * 50, "List of first 5 names", "-" * 50)
with open("names.txt", "r") as input_file:   # Prints list of names as visual
    print(input_file.read())
print("-" * 120)


# Q2

with open("names.txt", "r") as input_file:
    content = input_file.read()
    input_file.close()
    split_name = content.split("\n")
    search_name = input("Enter name you wanna search:")
# when search name is inside of split name then print
    if search_name in split_name:
        print("Name was in file")
# once name was not found allow user to append it to the names.txt
    else:
        y_n = input("Name was not found would you like to add it? Y / N ")
        if y_n == "Y":
            while len(search_name) < 10:
                search_name = input("Please enter name with 10 characters:")
            list_of_names.append(search_name)

            with open("names.txt", "w") as input_file:
                for item in list_of_names:
                    input_file.write(item + "\n")

# Visual showing new names from names.txt
            print("-" * 50, "New list with name added", "-" * 50)
            with open("names.txt", "r") as input_file:  # Prints list of names as visual
                print(input_file.read())
            print("-" * 120)

# If user chose N then do this
        else:
            if y_n == "N":
                print("-" * 120)
                print("Thank you for using name searcher!")
                print("-" * 120)

# Q3
import statistics                         # Import stats to use mean for average
print("-" * 50, "Question 3", "-" * 50)   # Visual
list_of_populatin = []                    # Declare empty list for population.txt
with open("population2.txt", "r") as file: # Reading from population.txt
        values = file.read().split("\n")  # Splitting pop.txt from \n onwards

for row in values:                        # For each row in values which is new split version
    col = row.split(" ")                  # split between each space
    list_of_populatin.append(int(col[2])) # and append col 2 (third value from 0 ,1 , 2)
print("Oldest:", max(list_of_populatin))  # Use those values to make max
print("Youngest:", min(list_of_populatin)) # Make min
print("Average:", statistics.mean(list_of_populatin)) # Make Average

