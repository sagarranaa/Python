# costructor parameter will dicided how much memory will take
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# compare Function(who is calling,whom to compare)
class Computer:
    def __init__(self):
        self.name="sagar"
        self.age=23
    # def upate(self):
    #     self.age=45

    def compare(self,other):
        if self.age==other.age:
             return True

        else:
             return False

c1=Computer() # this constructor
c1.age=80
c2=Computer()

if c1.compare(c2):
    print("They are same age")
else:
    print("they are different ")

print(c1.name)
print(c2.name)