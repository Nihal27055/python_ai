std = []
user = str(input("Enter first Student name : "))
usera = int(input(f"Enter the mark of {user} : "))
std.append(user)
user1 = str(input("Enter second Student name : "))
userb = int(input(f"Enter the mark of {user1} : "))
std.append(user1)
user2 = str(input("Enter third Student name : "))
userc = int(input(f"Enter the mark of {user2} : "))
std.append(user2)
user3 = str(input("Enter fourth Student name : "))
userd = int(input(f"Enter the mark of {user3} : "))
std.append(user3)
user4 = str(input("Enter fifth Student name : "))
usere = int(input(f"Enter the mark of {user4} : "))
std.append(user4)





std = {
    user : usera,
    user1 : userb,
    user2 : userc,
    user3 : userd,
    user4 : usere
}
grade = {}
if std[user] >= 90:
    grade[user] = "A"
elif 75 <= std[user] <= 89:
    grade[user] = "B"
elif 50 <= std[user] <= 74:
    grade[user] = "C"
else:
    grade[user] = "Fail"

gradea = {}
if std[user1] >= 90:
    gradea[user1] = "A"
elif 75 <= std[user1] <= 89:
    gradea[user1] = "B"
elif 50 <= std[user1] <= 74:
    gradea[user1] = "C"
else:
    gradea[user1] = "Fail"

gradeb = {}
if std[user2] >= 90:
    gradeb[user2] = "A"
elif 75 <= std[user2] <= 89:
    gradeb[user2] = "B"
elif 50 <= std[user2] <= 74:
    gradeb[user2] = "C"
else:
    gradeb[user2] = "Fail"

gradec = {}
if std[user3] >= 90:
    gradec[user3] = "A"
elif 75 <= std[user3] <= 89:
    gradec[user3] = "B"
elif 50 <= std[user3] <= 74:
    gradec[user3] = "C"
else:
    gradec[user3] = "Fail"

graded = {}
if std[user4] >= 90:
    graded[user4] = "A"
elif 75 <= std[user4] <= 89:
    graded[user4] = "B"
elif 50 <= std[user4] <= 74:
    graded[user4] = "C"
else:
    graded[user4] = "Fail"


result = {
    user: [std[user], grade[user]],
    user1: [std[user1], gradea[user1]],
    user2: [std[user2], gradeb[user2]],
    user3: [std[user3], gradec[user3]],
    user4: [std[user4], graded[user4]]
}

for name in result:
    print(f"Name: {name}   Mark: {result[name][0]}   Grade: {result[name][1]}")
