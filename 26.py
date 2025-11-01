list = []
user_name = input("Enter a name: ")
for i in range(1, 6):
    user_mark = int(input("Enter the mark: "))
    list.append(user_mark)

num = 0
for i in list:
    num = num + i

div = num / 5

if div >= 90 :
    print("Grade A")
elif 75 <= div <= 89 :
    print("Grade B")      
elif 50 <= div <= 74 :
    print("Grade C")      
elif div > 50  :
    print("Grade F")      
