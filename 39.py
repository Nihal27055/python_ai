try :
    user = int(input("Enter a num to divided byy 20 : "))
    num = 20
    print(num/user)
except ZeroDivisionError:
    print("20 divided by zero is not possible")
