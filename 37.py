user = str(input("Enter a word : ").capitalize())
with open("ex.txt","r") as file :
    r = file.read().split()
    count = 0 
    for i in r:
        if i == user :
            count += 1
    print(count)