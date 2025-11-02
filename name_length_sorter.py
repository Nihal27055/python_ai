# list = ["Zoe", "Alice", "Bob", "Eve", "Clara"]

# for i in range (len(list)):
#     for j in range (i + 1 ,len(list)):
#         if len(list[i]) > len(list[j]):
#             list[i],list[j]=list[j],list[i]

# print(list)


list =["Zoe", "Alice", "Bob", "Eve", "Clara"]
list.sort()
list.sort(key=len)
print(list)