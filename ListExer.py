#Index & List
Num=[45,875,2,67254,7587,2]
print(Num[-6])
### List of list
names=['Disha','Yogini','Shilpa']
#print(type([Num,names]))
listofList=[Num,names]
print([Num,listofList])
names.append('sagar')
print([Num,listofList]) ## append funcation will add the value ,it is mutuable
Num.clear() # Clear Function will clear the list of all values
print(Num)
names.insert(0,'kundan') #insert function will add the values where you will define
print(names)
names.remove('sagar') # This removes the value
print(names)
Num.pop()
print(Num) # This is datasctructure first come first out

del Num[0:2]
print(names)