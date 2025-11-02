with open ("ex.txt","r") as file :
    c = file.read()
    a = c.split()
    b = len(a)
    print(f"letters in file = {b}")