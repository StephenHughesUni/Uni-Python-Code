# Stephen Hughes
# 01/02/2021
# X00179579

# Q1

# Verifying Lists
Employee_PPS = []
Employee_GROSS = []
TYPE_A = 10000
TYPE_B = 20000
TYPE_C = 50000
tax_types = ["A","B","C","D"]
tax_amount =[]

NUM_OF_EMPLOYEE = 1

# Function
print("-" * 35)  # To add style
print("Welcome to Employee Tax Calculator")  # Welcome message

for employee in range(NUM_OF_EMPLOYEE):  # for index in range of 5 iterations.

    PPS_num = input(f"Enter Employee PPS {employee + 1}:")  # Asking user to enter info with each iteration showed
    Employee_PPS.append(PPS_num)  # Appending the user entered values to my PPS list

    gross_num = float(input(f"Please enter Employee {employee + 1} gross pay:"))  # Same as above for Gross
    Employee_GROSS.append(gross_num)  # Same as above for gross

    print(employee, "has a gross pay of $", Employee_GROSS[employee])
    if gross_num <= TYPE_A:
        print(f"Paid tax of $0   and has net pay of ${gross_num}")
        tax_amount = 0
    elif gross_num <= TYPE_B:
        tax = (gross_num - 10000) * 0.3
        gross_num = gross_num - tax
        print(f"Paid a tax of ${tax} and has net pay of ${gross_num}")
        tax_amount = tax
    elif gross_num <= TYPE_C:
        tax = (gross_num - 10000) * 0.35
        gross_num = gross_num - tax
        print(f"Paid a tax of ${tax} and has net pay of ${gross_num}")
        tax_amount = tax
    else:
        tax = (gross_num - 15000) * 0.4
        gross_num = gross_num - tax
        print(f"Paid a tax of ${tax} and has net pay of ${gross_num}")
        tax_amount = tax

print("-" * 35)  # To add Style
print("-" * 35)
print("{:<10}{:<10}".format("Employee", "Net Pay"))
for index, PPS_num in enumerate(Employee_PPS):
    print("{:10} {:<10}".format(PPS_num, Employee_GROSS[index]))
print("-" * 35)
