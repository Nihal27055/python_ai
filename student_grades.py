user1 = int(input("Enter the mark of nihal : "))
user2 = int(input("Enter the mark of mouz : "))
user3 = int(input("Enter the mark of saneen : "))
user4 = int(input("Enter the mark of sahal : "))
user5 = int(input("Enter the mark of mifzal : "))

std = {
    "nihal": user1,
    "mouz": user2,
    "saneen": user3,
    "sahal": user4,
    "mifzal": user5
}

grade = {}
if std["nihal"] >= 90:
    grade["nihal"] = "A"
elif 75 <= std["nihal"] <= 89:
    grade["nihal"] = "B"
elif 50 <= std["nihal"] <= 74:
    grade["nihal"] = "C"
else:
    grade["nihal"] = "Fail"

gradea = {}
if std["mouz"] >= 90:
    gradea["mouz"] = "A"
elif 75 <= std["mouz"] <= 89:
    gradea["mouz"] = "B"
elif 50 <= std["mouz"] <= 74:
    gradea["mouz"] = "C"
else:
    gradea["mouz"] = "Fail"

gradeb = {}
if std["saneen"] >= 90:
    gradeb["saneen"] = "A"
elif 75 <= std["saneen"] <= 89:
    gradeb["saneen"] = "B"
elif 50 <= std["saneen"] <= 74:
    gradeb["saneen"] = "C"
else:
    gradeb["saneen"] = "Fail"

gradec = {}
if std["mifzal"] >= 90:
    gradec["mifzal"] = "A"
elif 75 <= std["mifzal"] <= 89:
    gradec["mifzal"] = "B"
elif 50 <= std["mifzal"] <= 74:
    gradec["mifzal"] = "C"
else:
    gradec["mifzal"] = "Fail"

graded = {}
if std["sahal"] >= 90:
    graded["sahal"] = "A"
elif 75 <= std["sahal"] <= 89:
    graded["sahal"] = "B"
elif 50 <= std["sahal"] <= 74:
    graded["sahal"] = "C"
else:
    graded["sahal"] = "Fail"


print(std)
print(grade)
print(gradea)
print(gradeb)
print(gradec)
print(graded)
