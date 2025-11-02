accounts = {
    "Alice": {"owner": "Alice", "balance": 5000},
    "John": {"owner": "john", "balance": 10000},
    "Robby": {"owner": "robby", "balance": 4000}
}
user_choise =str(input("Withraw or Deposite : ").lower())


print(f"{accounts["Alice"]["owner"]}")
print(f"{accounts["John"]["owner"]}")
print(f"{accounts["Robby"]["owner"]}")

if "withraw" == user_choise :
    user = str(input("Which a account : ").capitalize())
    if user in accounts:
        print(f"balane : {accounts[user]['balance']}")
        user2 = int(input("How much to withraw : "))
        withraw = user2
        accounts[user]["balance"] -= withraw
        print(f"balane is : {accounts[user]['balance']}")
elif "deposite" == user_choise:
    user_deposite = str(input("Enter student name to deposite : ").capitalize())
    user_deposite2 = str(input("Enter whom from deposite : ").capitalize())
    if user_deposite and user_deposite2  in accounts :
        print(f"{user_deposite} balane : {accounts[user_deposite]['balance']}")
        print(f"{user_deposite2} balane : {accounts[user_deposite2]['balance']}")
        user_depo = int(input("How much to deposite : "))
        depo = user_depo
        accounts[user_deposite]["balance"] -= depo
        accounts[user_deposite2]["balance"] += depo
        print(f"balane is : {accounts[user_deposite]['balance']}")
        print(f"balane is : {accounts[user_deposite2]['balance']}")


