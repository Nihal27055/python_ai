accounts = {
    "std1": {"owner": "std1", "balance": 5000},
    "std2": {"owner": "std2", "balance": 10000},
    "std3": {"owner": "std3", "balance": 4000}
}
print("    daily getting    ")
print("       ")
deposit = 300
accounts["std1"]["balance"] += deposit
print(f"{deposit} added to std1")
deposit = 300
accounts["std2"]["balance"] += deposit
print(f"{deposit} added to std1")
deposit = 300
accounts["std3"]["balance"] += deposit
print(f"{deposit} added to std1")

print("       ")
print("       ")
print("    withraw money    ")
print("       ")
withraw = 750
accounts["std1"]["balance"] -= withraw
print(f"{withraw} minus from std1")
withraw = 200
accounts["std1"]["balance"] -= withraw
print(f"{withraw} minus from std1")
withraw = 3470
accounts["std1"]["balance"] -= withraw
print(f"{withraw} minus from std1")


print("       ")
print("       ")
print("    share to friends   ")
print("       ")
# std1 share the ammount to std2
share = 400
accounts["std1"]["balance"] -= share
accounts["std3"]["balance"] += share
print(f"std1 share {share} to std3")
# std1 share the ammount to std2
share = 905
accounts["std3"]["balance"] -= share
accounts["std2"]["balance"] += share
print(f"std3 share {share} to std2")
# std1 share the ammount to std2
share = 370
accounts["std2"]["balance"] -= share
accounts["std1"]["balance"] += share
print(f"std2 share {share} to std1")
# std1 share the ammount to std2
share = 90
accounts["std3"]["balance"] -= share
accounts["std1"]["balance"] += share
print(f"std3 share {share} to std1")
# std1 share the ammount to std2
share = 500
accounts["std3"]["balance"] -= share
accounts["std2"]["balance"] += share
print(f"std3 share {share} to std2")
print("       ")
print("       ")
print("    balance of each students    ")
print("       ")
# balance
print(f"std1 balance is :{accounts['std1']['balance']}")
print(f"std2 balance is :{accounts['std2']['balance']}")
print(f"std3 balance is :{accounts['std3']['balance']}")
