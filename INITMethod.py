# if we want to create any variable for storing valu .we should use __init__ method
# every object has it's own value or variable
class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("configure is : ",self.cpu,self.ram)
com1=Computer('i5 Processor','16 Gb')
com2=Computer('Ryzen3 Procesor','9 Gb')

com1.config()
com2.config()