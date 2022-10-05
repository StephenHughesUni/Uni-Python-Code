# Stephen Hughes
# 15/02/2021
# X00179579

total_results = 0
test_amount = 4
student_info = []
average = 0

for student in range(test_amount):
    test = []
    total = 0
    for index in range(4):
        print("*" * 40)
        results = float(
            input(f"Please enter what student {student + 1} got on test {index+1} :"))
        while results < 0 or results > 100:
            print("Result must be in range 0 to 100 try again.")
            results = float(
                input(f"Please enter what student {student + 1} got on test {index + 1} :"))
        total_results += results
        total += results
        test.append(results)
    test.append((total / 4))
    student_info.append(test)


print(total_results)
print(student_info)
total_average = total_results / 16

print(" ")
print("{0:20}{1:20}{2:20}{3:20}{4:20}".format(
    "\t\t\tTest 1", "Test 2", "Test 3", "Test 4", "Average"))
# Looping personal info columns
for each_student, i in enumerate(student_info):
    print(f"Student {each_student+1}: ", end="")
    for index, information in enumerate(i):
        print("{0:<20}".format(information), end="")
    print()

print()
print("The total average is", total_average)
