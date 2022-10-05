# Stephen Hughes
# 08/02/2021
# X00179579

salesreps = []
NUM_REPS = 4
total_sales = 0
num_exceeds = 0

Target = int(input("What would you like to set as the target? : "))

for rep in range(NUM_REPS):
    sales = []
    for i in range(5):
        sale = int(input(f"Please enter how much employee {rep+1} has made on day {i+1}:"))
        total_sales += sale
        sales.append(sale)
    salesreps.append(sales)
    print("-" * 50)

for index in range(NUM_REPS):
    print(f"Employee rep {index+1}'s total ", end="")
    sales = sum(salesreps[index])
    print(sales)
    if sales > Target:
        num_exceeds += 1
        print("Has exceeded target goal")
    print("-" * 50)

print(" ")
print("{0:20}{1:20}{2:20}{3:20}{4:20}".format("\t\tDay 1", "Day 2", "Day 3", "Day 4", "Day 5"))
for rep_people, i in enumerate( salesreps):  # Looping personal info columns
    print(f"Rep {rep_people+1}: ", end="")
    for index, information in enumerate(i):
        print("{0:<20}".format(information), end="")
    print()

print(" ")
print("The total of everyone is", total_sales)
print("The number of people who exceeded their sale", num_exceeds)
