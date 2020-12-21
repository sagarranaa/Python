# basically their are two type of variable in function
#gloable variable - this variable can access any where inside function or outside as well
# loaction
a=10 # global variable
print(id(a))
def something():
    #if your intension is to change global variable then use global keyword
    # global a
    # if we want to print all global variable inside my function use gloabls() with key or value pair
     # we can't change both  variable at time local variable or global variable
    a=100
    x=globals()['a']
    print(id(x))
    globals()['a']=20
    #a=5 # local variable
    print("local vairable",a)

something()
print("global variable",a)

