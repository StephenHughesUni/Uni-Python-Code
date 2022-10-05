# Stephen Hughes
# X00179579


# Adding
def adding(num1, num2):
        return num1 + num2
# Subtracting
def subtract(num1, num2):
    return num1 - num2
# Multplying
def multiply(num1, num2):
    return num1 * num2
# Dividing
def divide(num1, num2):
    return num1 / num2
# Power
def power(num1, num2):
    return num1 ** num2
# List of powers
def powerlist(num1, num2):
    power_list = []
    for i in range(num1, num2 + 1):
        square = i ** 2
        print(square)
        power_list.append(square)
# Count a string
def stringcount(str1):
    count1 = 0
    count2 = 0
    for i in (str1):
        if (i.islower()):
            count1 = count1 + 1
        elif (i.isupper()):
            count2 = count2 + 1
    print("in string:", str1)
    print("lower case letters appear", count1, "times")
    print("upper case letters appear", count2, "times")
# Change the temp
def tempchanger(num1=None):
    if num1 is None:
        print("No argument for celsius")
    else:
        farenheit = round(((num1 * 1.8) + 32), 2)
        print(num1, "celsius converted to fharenheit:", farenheit)
# Menu display
def display_menu():
    print("*" * 29)
    print("*\t\tCalculator+\t\t\t*")
    print("\t 1- Add ")
    print("\t 2- Subtraction ")
    print("\t 3- Multiplication ")
    print("\t 4- Division ")
    print("\t 5- Raise to the power ")
    print("\t 6- List of squares ")
    print("\t 7- Upper and Lower Case ")
    print("\t 8- Concert Temperature ")
    print("\t 9- Exit ")
    print("*" * 29)
display_menu()
menu_option = int(input("\tPlease enter menu option:"))

# Options
while menu_option != 9:
    if menu_option == 1:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print(number1, "+", number2, "=", adding(number1, number2))
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))
    elif menu_option == 2:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print(number1, "-", number2, "=", subtract(number1, number2))
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))
    elif menu_option == 3:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print(number1, "*", number2, "=", multiply(number1, number2))
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))
    elif menu_option == 4:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        while number2 == 0:
            number2 = int(input("Invalid option, re-enter:"))
        print(number1, "/", number2, "=", divide(number1, number2))
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))
    elif menu_option == 5:
        number1 = int(input("Enter first number: "))
        while number1 <= 0:
            number1 = int(input("Invalid option, re-enter:"))
        number2 = int(input("Enter second number: "))
        while number2 <= 0:
            number2 = int(input("Invalid option, re-enter:"))
        print(number1, "**", number2, "=", power(number1, number2))
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))
    elif menu_option == 6:
        number1 = int(input("Enter start value: "))
        number2 = int(input("Enter end value: "))
        print("Start value:", number1, "End value:", number2,"\n----List of their powers----")
        powerlist(number1, number2)
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))
    elif menu_option == 7:
        string1 = input("Enter string:")
        stringcount(string1)
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))
    elif menu_option == 8:
        celsius = float(input("Enter temperature in celsius:"))
        tempchanger(celsius)
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))




