class Student:
    def __init__(self,name,rollNumber):
        self.name=name
        self.rollNumber=rollNumber
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollNumber)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.processor="Intel i5"
            self.Brand="HP"
            self.ram="16 Gb"
        def show(self):
            print(self.processor,self.Brand,self.ram)

s1=Student('sagar',178)
s1.show()
