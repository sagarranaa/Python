# there are two type of variable 1.class variables 2. instance variable
class Car:
    wheel=4
    def __init__(self):
        self.Mileage="50 Km/h"
        self.companyName="BMW"
c1=Car()
c2=Car()
c1.companyName="Lomborgini"
c2.wheel=10
print("Mileage is: ",c1.Mileage,"companyName is:",c1.companyName ,"and wheel is:",c1.wheel)
print("Mileage is: ",c2.Mileage,"companyName is:",c2.companyName, "and wheel is:",c2.wheel)