f = open("ex.txt", "a+")
f.write("\nHello Python")
f.seek(0)
print(f.read())
f.close()

