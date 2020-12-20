# from numpy import *

# arr1=array([[
#
#     [1,212,456],
#     [5,4,5756],
#     [1,2,3]
# ]])
#
# print(arr1.ndim)
# print(arr1.shape)
# # flattern function will flattern ur array into 1d
# arr2=arr1.flatten()
# print(arr2)
#
# # reshape is will change ur array in ur gievn format
# arr2.reshape(2,3)


# arr1=array([
#     [1,2,3,4,5,6],
#     [8,7,9,8,1,3]
# #
# ])
# # arra2=arr1.flatten()
# # arra3=arra2.reshape(2,2,3)
# # print(arra3)
#
# m=matrix(arr1)
# print(diagonal)
import numpy as np

array1=np.array([
    [1,2,3,4,5,6]
    # [7,7,8,9,5,2]


])
array2=np.array([
    [7,5,2,1,2,3]
    # [1,2,3,6,2,4]
])
print("First Array",array1)
print("second Array",array2)

output1=np.multiply(array1,array2)
print("The multification of 2 array is :",output1)