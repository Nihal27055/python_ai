try :
    with open("er.txt","r") as file :
        read = file.read()
except FileNotFoundError :
    print("file not exisit")



    