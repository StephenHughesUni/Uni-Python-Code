# Stephen Hughes
# 01/02/2021
# X00179579

# Lab 2

# Lists etc
names = []
total_sales = []
COMMISSION_BOUND = 50000
COMMISSION_PERCENT = 0.15
sales = 0
commission_value = 0

# Welcome message
print("-" * 50)
print("\t\t\t   Kitchen Sales System")
print("-" * 50)

# User input of how many times to run
kitchen_sellers = int(input("Number of Salesmen:"))

# For loop to ask name and kitchen sold
for num in range(0, kitchen_sellers):
    seller_name = input("Name of salesman:")
    names.append(seller_name)
    kitchen_sales = int(input("Number of Kitchens Sold:"))

# For loop within to ask price of kitchen to then append to sales
    for i in range(kitchen_sales):
        kitchen_price = float(input("Price of kitchen:" + str(i + 1) + ":£"))
        sales += kitchen_price
    total_sales.append(sales)

# if the sales are greater than the commission bound do...
    if sales > COMMISSION_BOUND:
        commission_value = round(COMMISSION_PERCENT * (sales - COMMISSION_BOUND), 2)
        print("Commission payable for {}: £{}".format(seller_name, commission_value))
        print("-" * 50)
    # print("Commission payable for", seller_name, total_sales)
    # commission_value = round(COMMISSION_PERCENT * (sales - COMMISSION_BOUND), 2)
    else:
        print("No commission payable for", seller_name)
        print("-" * 50)
        print("-" * 50)
        print("-" * 50)
    sales = 0

# formatting the prints
print("{:<10}{:<10}".format("Employee", "Total Sales"))
for num in range(kitchen_sellers):
    print("{:10} {:<10}".format(names[num], total_sales[num]))
print("-" * 50)

# Min and Max positioning with index
max_sale = max(total_sales)
min_sale = min(total_sales)

min_i = total_sales.index(min_sale)
max_i = total_sales.index(max_sale)

# Output / final prints with formats
print("Total commission paid: £{}".format(commission_value))
print("Highest sales made: £{} by {}".format(max_sale, names[max_i]))
print("Lowest sales made: £{} by {}".format(min_sale, names[min_i]))
print("Sales values in ascending order")
print(*sorted(total_sales), sep="\n")
