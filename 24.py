list1 = []
for i in range(1,7):
    user = input("Enter a word : ")
    list1.append(user.lower())   
list2 =[]
for word in list1:
    for i in list1 :
        if word != i and sorted(word) == sorted(i):
            list2.append(word)
            break
list(list1)
print(" Anagram words only:", sorted(set(list2)))
