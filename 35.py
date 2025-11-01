with open("ex.txt","r") as file :
    r = file.read()

with open("copy.txt","w") as file:
    w = file.write(r)