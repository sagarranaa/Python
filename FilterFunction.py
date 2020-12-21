from functools import reduce
# Filter function will just filter all things from a  list
num=[12,45,786,245456,45132,12765,45321,2312,4542,121,123,4545,4531,3235,746545,1321,1]
even=list(filter(lambda x: x%2==0,num))
#map function will perform operation
print(even)
double=list(map(lambda x:x*2,even))
print(double)
# reduce will reduce anything 3 one more important thing that you have import reduce function from a module
Reduce=reduce(lambda x,y:x+y,double)
print(Reduce)
