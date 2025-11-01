with open("ex.txt","r") as file :
    r =file.readlines()
    r.reverse()
    
with open("copy.txt","w") as file :
    w = file.writelines(r)