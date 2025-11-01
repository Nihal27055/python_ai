guess = 3
while True :
    user = int(input("Enter your guess : "))
    if user == guess :
        print("Correct answer")
        break
    else :
        print("Wrong answer try again")    