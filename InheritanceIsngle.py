# Inheritance method  single level and multilevel inheritances
class Super(): #parent
    def feature1(self):
        print("this is super class working 1")
    def feature2(self):
        print("this is super class working 2:")
class SubClass(Super): #child class
    def feature3(self):
        print("this is subclass working 1")
    def feature4(self):
        print("this is subclass working 2")
class Multilevel(SubClass): # multilevel class inheritance
    def feature5(self):
        print("this is multilevel class feature1")
    def feature6(self):
        print("this is multilevel class feature6")
s1=Super()
s1.feature1()
s1.feature2()
b1=SubClass()
c1=Multilevel()
b1.feature2(),b1.feature2(),b1.feature3(),b1.feature4()
c1.feature5()
c1.feature6()
c1.feature2()


