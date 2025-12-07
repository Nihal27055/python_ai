class car :
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def car_details(self):
        print(f"Car Brand is {self.brand}")
        print(f"Car Model is {self.model}")

cars = car(str(input("Enter Car brand : ")),str(input("Enter Car model : ")).capitalize())
cars.car_details()