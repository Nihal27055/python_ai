while True :
    print("1.Add")
    print("2.Sub")
    print("3.Mult")
    print("4.Devision")

    a = int (input ("Enter 1/2/3/4 : "))
    num1 =int (input("Enter your number :  "))
    num2 =int (input("Enter your number :  "))

    if (a == 1) :
        print(num1+num2)
    elif (a == 2) :    
        print(num1-num2)
    elif (a == 3) :    
        print(num1*num2)
    elif (a == 4) :    
        print(num1/num2) 
    cont = str(input("Do you want to continue this yes/no : ")).lower()
    if cont != "yes":
        print("Bye")
        break
