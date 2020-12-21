def res(n):
    if n==1:
        return 1
    else:
        return n*res(n-1)
x=int(input("Enter a number which will give Recurrsion of it:?\n"))
result=res(x)
print(result)