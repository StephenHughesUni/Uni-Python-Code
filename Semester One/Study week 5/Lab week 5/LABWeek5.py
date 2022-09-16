# Stephen Hughes
# X00179579  - 09/11/2020
# This program will have a user enter details and give gross pay, tax amount and net pay

# Inputs
Employ_ID = str(input("Enter your employee ID: "))
name = str(input("Please enter your full name: "))
address = str(input("Please enter your address: "))
marital_status = str(input("Please enter S if single and M if married: "))
gross_pay = float(input("Please enter gross pay: "))

# Constants
ALLOWANCE1 = 25000
ALLOWANCE2 = 20000
ALLOWANCE = 0

S_TAX = 0.20
M_TAX = 0.23

# Process
if gross_pay < 50000:
    ALLOWANCE = ALLOWANCE1
elif gross_pay >= 50000:
    ALLOWANCE = ALLOWANCE2


if marital_status == "S":
    TAX = S_TAX
    marital_status = "single"
elif marital_status == "M":
    TAX = M_TAX
    marital_status = "married"
else:
    TAX = 0
    marital_status = "null"

tax_paid = (gross_pay - ALLOWANCE) * TAX
net_pay = gross_pay - tax_paid

# Printing
print("")
print("******************************************")
print("Employee ID:", Employ_ID, "\n" "Name:", name, "\n" "Address:", address, "\n" "Marital Status:", marital_status,
      "\n" "Entered gross pay:", gross_pay)
print("The total tax paid from your gross after applying your allowance and tax is: ", tax_paid)
print("The total net pay after applying your gross pay and tax pay is:", net_pay)
print("*****************************************")
password = input("Please Enter Your Password")
password_confirm = input("Please Confirm Your Password")
# Password check
if password == password_confirm:
    print("Password has been set and is matching.")
else:
    print("Your password does not match")
print("*****************************************")
