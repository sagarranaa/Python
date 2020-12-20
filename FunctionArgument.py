# in function their are two type of argument # formal argument # actual argument
# def add(a,b): # formal argument
   # c=a+b
    #print(c)
# add(5,5) # actual argument

#add(b=5, a=6)# if we don't know sequence of calling argument simply we pass keyword of argument and value

#def PersonName(name,age=18): # Default argument age is here
    #print(name)
    #print(age)
#PersonName("sagar") # if u gave parameter but it has already default argument then in this case it weill override

# Antoher example (length of argument) what if user in giving ulimited parament but he want to also

# def add(x,*b):
#     c=x
#     for i in b:
#         c=c+i
#     print(c)
# add(2,5,7,5,2)
# another way
def add(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
add(2,5,7,5,2)