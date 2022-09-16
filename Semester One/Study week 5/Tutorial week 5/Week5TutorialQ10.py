# EC
# 13/11/2020
# Tutorial Solution
# Q 10
username = input("Username: ")
password = input("Password: ")
security = 0
if username == "guest":
    if password == "guest":
        print("Guest login granted")
        security = 1
    else:
        print("Guest login denied...Invalid Password")
elif username == "M.Dawson":
    if password == "nos123":
        print("Welcome", username, "Login granted")
        security = 5
    else:
        print(username, "Login denied ... password incorrect")
else:
    print(username, "not recognised - access denied")

print("Security Level Granted: ", security)
