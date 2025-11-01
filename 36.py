with open("ex.txt","r") as file :
    count = file.read()
    c = len(count)
    print(c)

with open("ex.txt","r") as file :
    words = file.read()
    wr = words.split()
    w = len(words)
    print(w)

with open("ex.txt","r") as file :
    line = file.readlines()
    lines = len(line)
    print(lines)                 