# Stephen Hughes
# 08/02/2021
# X00179579


# Initializing my lists and totals
personal_info = []
total_votes = 0
people = 4
# All below is for who won - winner / loser
high_vote = 0
winner = ""
low_vote = 999999999999999
loser = ""

# Collecting information in range.
for cand in range(people):
    print("*" * 40)
    lastname = input(f"Please enter last name of candidate {cand + 1} :")
    number_votes = int(input(f"Please enter number of votes of candidate {cand + 1} :"))
    total_votes += number_votes  # Adding each entered votes together
    constituency = input(f"Please enter location of candidate {cand + 1} : ")
    candidate = [lastname, number_votes, constituency]  # Putting all 3 information together
    personal_info.append(candidate)  # Appending it all
    # Below used for finding winner and loser from top of code.
    if number_votes > high_vote:
        high_vote = number_votes
    if number_votes < low_vote:
        low_vote = number_votes

# Formatting the headings
print("{0:20}{1:20}{2:20}{3:20}".format("Name", "Votes", "Constituency", " % "))
print("-" * 80)
for candidate in personal_info:  # Looping personal info columns
    for i, information in enumerate(candidate):
        print("{0:<20}".format(information), end="")
    percent = round(((candidate[1] / total_votes) * 100), 2)  # Adding the % column with maths added.
    print("{0:<20}".format(percent), end="")
    print()
    # Checking if high votes ( from top of page ) is within candidate then the winner is index 0.
    if high_vote in candidate:
        winner = candidate[0]
    # Same as above but for low votes and loser.
    if low_vote in candidate:
        loser = candidate[0]

# Printing the winner and loser
print(f"Winner is: {winner}")
print(f"Loser is: {loser}")

"""
for row in personal_info:
    for col in row:
        print("{0:10}".format(col), end="")
    print()
"""
