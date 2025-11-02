num = int (input("Enter a number : "))
if num % 2== 0 :
    print ("even")
    if num < 50 :
        print("lessthan 50")      
elif num % 2 != 0 :
    print("odd")
    if num < 10 :
        print("lessthan 10")
    else :
        print ("greaterthan 10")        
        