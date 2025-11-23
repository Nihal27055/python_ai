class car_s :
    def __init__(self, brand , model):
        self.model = model
        self.brand = brand
    def cars (self):
        print(f"car : ",self.brand ," , ",self.model)



user = str(input("Enter a car brand : "))
user1 = str(input("Enter a car model : "))


car = car_s(user,user1)
car.cars()