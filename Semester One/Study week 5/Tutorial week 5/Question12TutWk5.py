# Stephen Hughes
# Tutorial Solutions
# Question 12 Week 5

security = 0
username = input("Username: ")
password = input("Password: ")
# processing
if username == "M.Dawson" and password == "nos123":
    security = 5
    print("Welcome", username)
elif username == "W.Wright" and password == "einstein":
    security = 3
    print("Welcome", username)
elif username == "J.Brown" and password == "Victorian":
    security = 3
    print("Welcome", username)
elif username == "guest" or password == "guest":
    security = 1
    print("Welcome Guest")
else:
    print("Access denied ... incorrect login")

print("Security level granted:", security)
