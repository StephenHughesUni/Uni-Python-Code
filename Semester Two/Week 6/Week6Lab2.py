# Stephen Hughes
# X00179579
# 01/03/2021

# Display employee with formatting using enumerate for each item / row placement
def display_employee():
    print("-" * 105)
    print("{0:20}{1:20}{2:20}{3:20}{4:20}{5:20}".format(
        "Staff ID", "Employee Name", "Commencement Date", "Grade", "Salary", "Bonus"))
    for item, i in enumerate(staff_list):
        for index, information in enumerate(i):
            print("{0:<20}".format(information), end="")
        print()
# Shows total number of employees
    print("-" * 32)
    print(f"Number of Total Employee's : {item+1}")
    print("-" * 32)

# Finding employee number based on two inputs of the staff list and the input from user
def search_emp(input_list, input_id):
    key = False
    for i, item in enumerate(input_list):
        if input_list[i][0] == input_id:
            key = True
            print("-" * 15, "Found Employee", "-"* 15)
            print(*input_list[i], sep=", ")
            print("-" * 46)
    if not key:
        print("-"*30)
        print("Employee number not found")
        print("-"*30)

# Gets the calculation of the bonus by splitting the information apart and using it in the calculation to 0.01 1%
def calc_bonus(input_list):
    import time
    for i, row in enumerate(input_list):
        date_split = row[2].split("/")
        year_split = date_split[2]  # split row 2 (date row)
        y = int(time.strftime("%Y"))  # y is year
        years_at_company = y - int(year_split) # current year - the split year from list
        salary_split = row[4]
        # Calculating bonus
        total_bonus = salary_split * 0.01 * years_at_company
        # Changing bonus
        staff_list[i][5] = round(total_bonus, 4)

# The menu
def display_menu():
    print("*" * 29)
    print("*\t\tHR Department \t\t*")
    print("*" * 29)
    print("*\t 1) Add Employee \t\t*")
    print("*\t 2) List Employees\t\t*")
    print("*\t 3) Search Employee\t\t*")
    print("*\t 4) Set Bonus\t\t\t*")
    print("*\t 5) Exit\t\t\t\t*")
    print("*" * 29)
display_menu()

# The list
staff_list = [[100, "Jack Jones", "01/10/2000", 5, 60000, 0],
              [200, "Mary Smith", "01/07/2000", 6, 70000, 13300],
              [300, "Patrick Bennett", "01/11/2001", 6, 70000, 12600],
              [400, "Ann Lewis", "01/12/2011", 4, 40000, 3200],
              [333,	"Ken White", "01/01/2010", 4, 40000, 3600]]

# Let the user have a input for menu
menu_option = int(input("Please enter option:"))
# Each option
while menu_option != 5:
    if menu_option == 1:
        for i in range(1):
            Employee_info = []
            Employee_info.append(int(input("Employee ID:")))
            Employee_info.append(input("Employee Full Name:"))
            Employee_info.append(input("Commencement Date (Ex 03/04/2020):"))
            Employee_grade = int(input("Empoyee Grade:"))
            if Employee_grade > 8 or Employee_grade < 4:
                Employee_info.append(int(input("Enter Valid Grade 4 - 8 -Empoyee Grade:")))
            else:
                Employee_info.append(Employee_grade)
            Employee_info.append(int(input("Employee Salary:")))
            Employee_info.append(0)
            staff_list.append(Employee_info)
            display_menu()
            menu_option = int(input("\tPlease enter menu option:"))

    if menu_option == 2:
        display_employee()
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))

    if menu_option == 3:
        search_key = int(input("Enter ID you wish to search:"))
        search_emp(staff_list, search_key)
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))

    if menu_option == 4:
        calc_bonus(staff_list)
        display_menu()
        menu_option = int(input("\tPlease enter menu option:"))