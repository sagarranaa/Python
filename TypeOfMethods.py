class Student:
    college="Viva college virar west "

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1 +self.m2 + self.m3)/3
# we want to get college name then use decorator @ symbol
    @classmethod
    def getCollege(cls):
        return cls.college
    #staticmethod
    @staticmethod
    def info():
        print("This is Student class ... in ABC module")
s1=Student(88,50,45)
s2=Student(20,45,60)
print(Student.getCollege())
print(s1.avg())
print(s2.avg())
Student.info()


