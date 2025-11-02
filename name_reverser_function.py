def reverse(a,b):
    for name in a :
        b = name + b
    print(f"Your name reverse : {b.capitalize()}")     
word = ""
user = input("Enter Your Name : ")
reverse(user,word)  

