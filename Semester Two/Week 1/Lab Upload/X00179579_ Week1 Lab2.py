"""
Stephen Hughes - X00179579
Week1 - Lab 2 - Lists Exercise 1
"""
# Lists
candidates_list = []
vote_list = []
candidate_amount = 5
total_votes = 0

# Loop to append list
for i in range(candidate_amount):
    candidates_list.append(input(f"Please enter the last name of candidate {i+1}:"))
    vote_list.append(int(input(f"What were the total votes for {candidates_list[i]}:")))

# Second loop
for i in range(int(len(candidates_list))):
    total_votes += vote_list[i]

# Header
print("Candidate\t\tVotes\t\t % Votes")

# Positioning and % vote
for i in range(int(len(candidates_list))):
    percent_vote = (vote_list[i] / total_votes) * 100
    print(f"{candidates_list[i]:12}{vote_list[i]:8}\t\t{percent_vote:.2f}")

# Maths
total_votes = sum(vote_list)
average = total_votes / candidate_amount
Max = vote_list.index(max(vote_list))
Min = vote_list.index(min(vote_list))

# Output
print(f"\nTotal:\t{total_votes} \nAverage:\t{average} \n\nWinner:\t{candidates_list[Max]} \nLowest Votes:\t{candidates_list[Min]}")

'''
# Question 2


# Lists declared
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
week_days = []
hourslist = []

for i in range(5):
    assistant_hours = float(input(f" How many hoers did you work on: {days_of_the_week [i]}:"))
    week_days.append(assistant_hours)

print(f"Assistant worked:{week_days}")
'''
