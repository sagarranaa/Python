# Inheritance method  single level and multilevel inheritances
class Super(): #parent
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("this is super class working 1")
    def feature2(self):
        print("this is super class working 2:")
class SubClass(): #child class
    def __init__(self):
        # if suppose we want to call both __init()__ then use keyword super.__init()__
        super().__init__()
        print("in B init")

    def feature3(self):
        print("this is subclass working 1")
    def feature4(self):
        print("this is subclass working 2")
class SubClass2(Super,SubClass):
    def __init__(self):
        super().__init__()
        print("in C init")
# s1=Super() #constructor1
c1=SubClass2() #constructor2
