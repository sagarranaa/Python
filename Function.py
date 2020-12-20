# printing hello by using function

# def gret_morning():
#     print("Hello")
#     print("Good Morning Alien")
# gret_morning()

# User defind function
# def addition():
#     x=int(input("Enter first number:"))
#     y=int(input("Enter Second Number:"))
#     c=x+y
#     print(c)
# addition()


# another example
# def sagar(x,y):
#     c=x+y
#     return  c
# result=sagar(5,5)
#
# print("The addition of two number is :",result)

# How to work with two variable function

def add_sub(x,y):
    c=x+y
    d=x-y
    e=x*y
    return c,d,e
result1,result2,result3=add_sub(8,7)
print(result1,result2,result3)