# array will take same datatype of value
from array import *
# vals=array('i',[12,5,4,7,85,87,4])
#
# print(vals.buffer_info()) # . buffer_info will give an array size

# val=array('f',[1.1,25.3,69.2,3.6,9.6])
# val.append(63)
# for i in range(0,4):
#     print(val[i])

# if we don't the length of array we can use len() function

# for i in range(len(val)):
#     print(val[i])

# val=array('u',['A','B','C','D','E','F','G','H','I'])
#
# for i in val:
#     print(i)

# val=array('i',[1,2,3,5,4,7,8,5,6,5])

# newArray=array(val.typecode,(a*a for a in val)) #list comoperision  loop

# for e in newArray:
#     print(e)
# same thing but by using while loop

# i=0
# while (i<len(newArray)):
#     print(newArray[i])
#     i=i+1

# write a code to sort the array in ascending order
val=array('i',[1,2,3,5,4,7,8,5,6,5])
print(sorted(val))