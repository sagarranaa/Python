# Taking the input from user side and printing factorial
def fact(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
x=int(input("enter number which will give you factorical of number: ?\n"))
result=fact(x)
print(result)