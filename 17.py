user = input("Enter a Word: ")
vowel = ["a","e","i","o","u"]

count = 0
for letter in user:
    if letter in vowel:
        count =count + 1

print("vowels = ",count)
