f = open("ex.txt", "a+")#permission
f.write("\nHello Python")
f.seek(0)#restart
print(f.read())
f.close()
