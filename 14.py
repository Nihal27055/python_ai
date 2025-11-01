num = []
nums = int(input("Enter how much you want to add : "))
for i in range(1,nums+ 1):
    user =int(input(f"Enter a number{i}: "))
    num.append(user)


print(f"list of num : {num}")   
print("Sum of numbers: ",sum(num))
