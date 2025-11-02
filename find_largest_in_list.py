list = []
rang = int(input("Enter how much num : "))
for i in range(rang):
    user =int(input(f"Enter a your { i+1} number : "))
    list.append(user)

larg = list[0]

for user in list:
    if user > larg:
        larg = user
print("largest number is ",larg)        