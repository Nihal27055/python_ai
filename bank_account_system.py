class account :
    def __init__(self,acc_name,name,balance):
        self.acc_name = acc_name
        self.name = name
        self.balance = balance
    def balnce(self):
        print(f" Account Balance {self.balance}")     
    def depo(self,num) :
        d = self.balance + num
        print(f"Money Deposited to Account {d}")
    def withr(self,num):
        e = self.balance - num
        print(f"Money Withraw From this Account {e}")

user = account(str(input("Enter Your Account Name : ")),str(input("Enter Your Name : ")),int(input("Add Some Money to the Account : ")))

user1 = str(input("Enter Deposite or Withraw or Check balance : ").lower())
while True :
    if user1 == "deposite":
        use = int(input("Deposite Money To The Account : "))
        a = user.depo(use)
    elif user1 == "withraw" :
        userr = int(input("Withraw Money From The Account : "))
        b = user.withr(userr)
    elif user1 == "balance" :
        user.balnce()
    u = str (input("Do you want to exit from this : "))
    if u == "yes" :
        break
