grade = int(input("Please enter your grade :"))
if grade <35:
    print("F")
elif grade <= 39:   # Trapping values between 35 - 39
    print("D")
elif grade <=49:
    print("C")
elif grade <=54:
    print("C+")
elif grade <=59:
    print("B-")
elif grade <=69:
    print("B")
elif grade <=79:
    print("B+")
else:
    print("A")