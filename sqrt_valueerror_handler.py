import math

try:
    number = int(input("Enter a num : "))
    square_root = math.sqrt(number)
    print(square_root)
except ValueError :    
    print("negative num not allowed")

