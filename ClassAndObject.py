# remember one if you want to use method(funciton) we have to use classname then . then function

class Computer: # attribute or blueprint
    def config(self):
        print("i5 , 16Gb , 1TB")
# here we will be using function by calling class name
#com1=Computer()  # here com1 is object .without object we can access anythin of class
#Computer.config(com1) # inside config method we have to  use object name
# another way for access
com1=Computer()
com2=Computer()
com1.config() # here by default config function will take self parameter
com2.config() 