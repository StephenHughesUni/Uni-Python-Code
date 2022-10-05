# SH
# 24/02/2021
# Tut Solution

# Q1 checking if number is within range
def test_range(n, start, end):
    # if start >=n <=end:
    if n in range(start, end + 1):
        print(n, "yes it is in")
    else:
        print(n, "nope")


test_range(10, 10, 20)



# Q2 - Splits string on comma and makes it into a 1D list and formats it.
def list_modules(modules_in):
    modules_list = modules_in.split(",")
    print(modules_list)
    print("The amount of models available:", len(modules_list))
    for i, item in enumerate(modules_list):
        print("Module {}: {}".format(i + 1, item))


# main code
list_modules("Software Development 2,Statistics,Operating Systems,Database Systems")



# Q3 -
def raise3(list_in):
    print(list_in)
    for i, item in enumerate(list_in):
        list_in[i] = item ** 3
    print(list_in)


# main code
original_list = [1, 2, 3, 4]
raise3(original_list)
print(original_list)



# Q3
def multiples(list_in):
    multiples_list = []
    for number in list_in:
        if number % 10 == 0:
            multiples_list.append(number)
    print(multiples_list)


original_list = [10, 11, 40, 34, 32, 45, 50, 66, 70]
multiples(original_list)



def sum_rows(list2D_in):
    totals = []
    for row in list2D_in:
        row_sum = sum(row)
        totals.append(row_sum)
    print(totals)


nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
sum_rows(nums)
