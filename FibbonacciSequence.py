# # fibbonacci Series
# def fib(n):
#     a=0
#     b=1
#     if n<1:
#         print("Not a positive number")
#     if n==1:
#         print(a)
#
#
#
#     else:
#         print(a)
#         print(b)
#
#         for i in range(2,n):
#
#             c=a+b
#             a=b
#             b=c
#             print(c)
# fib(5)


def fib(n):

    a=0
    b=1
    c=0
    if n>=0:
        for x in range(n):
            print(a)
            c=a
            a=b
            b=a+c
    else:
        print("invalid")
a=int(input("Enter the number till which you want to print the series: ?\n"))
fib(a)