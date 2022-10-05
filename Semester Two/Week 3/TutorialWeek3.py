"""
# Q2

pic = []
for i in range(6):
    row = []
    for j in range(6):
        if i == j or i == 0 or i == 5:
            row.append("*")
        else:
            row.append(".")
    pic.append(row)

for row in range(6):
    for col in range(6):
        print(pic[row][col], end="")
    print()

# Q3
beta = []
for i in range (3):
    row = []
    for j in range(3):
        row.append(i + j)
    beta.append(row)
print(beta)


# Q4
num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
sum_list = []
for row in num:
    total = sum(row)
    sum_list.append(total)
print(sum_list)

max_sum = sum_list[0]
max_index = 0
for index, sum_value in enumerate(sum_list):
    if sum_value > max_sum:
        max_sum = sum_value
        max_index = index
print("Max total:", max_sum, "found at position:", max_index + 1)

# or
max_sum = max(sum_list)
max_index = sum_list.index(max_sum)
print("Max total:", max_sum, "found at position:", max_index + 1)

"""

match_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for word in match_list:
    if len(word) > 1 and word[0] == word[-1]:
        count += 1
print("Number of matches:", count)