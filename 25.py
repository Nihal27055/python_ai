def para(a):
    words = a.lower().split()
    wordss = {}
    for word in words:
        word = word.strip(".,!?")
        if word in wordss:
            wordss[word] += 1
        else:
            wordss[word] = 1
    return wordss

ab = "Python is fun. Python is easy to learn. Learning to Python makes programming to enjoyable."
print(para(ab))
