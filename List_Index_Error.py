list = ['10','20','30']
user = int(input("Enter a index number in the list : "))
try :
    num = list[user]
    print(num)
except IndexError :
    print("the index number not exisiting")
except NameError :    
    print("name error")
