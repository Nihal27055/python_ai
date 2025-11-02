with open("ex.txt","w") as file :
    file.write("this is a appended line . ")
with open("ex.txt","r") as file :
    a = file.read()
    print(a)