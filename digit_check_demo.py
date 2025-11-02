user = input("Enter a num : ")
if user.isdigit():
    user = int(user)
    if user > 0:
        print("Positive")
    elif user == 0:
        print("Zero")
    else:
        print("Negative")
else:
    print("Invalid number")
