user1 = int(input("Enter number you want to divided by : "))
user2 = int(input("Enter number you want to divided by : "))
try :
    num = (user1/user2)
except ZeroDivisionError:
    print("not available for divided by zero")      

print(num)
