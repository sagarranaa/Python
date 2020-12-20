from numpy import *
# arr=arange(1,6)
# for i in arr:
#     print(i+5)

# their are two way to copy any array
#1. view() # function
#2.copy()
# arr=arange(1,11)
# a=arr.copy()
# a[2]=8 # here we are changing the value of a which i had copied previously basically their are two type of copy function shallow copy or deep coopy
# print(arr)
# print(a)
# print(id(arr))
# print(id(a))

# Assignment
# 1.write a code to add 2 array using forloop

arr1 = array([5, 10, 15, 20, 30])
arr2 = array([55, 16, 1, 280, 60])
arr3 = ([])
k = 0
for num1 in arr1:
    num3 = num1 + arr2[k]
    arr3.append(num3)
    k += 1
print(arr3)
## 2.
value=arange(0,5)
print(max(value))
