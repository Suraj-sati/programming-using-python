import numpy
from functools import reduce
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)

mul=1
for i in l:
    mul=mul*i
print("multiply of elements in list is {}".format(mul))

x=numpy.prod(l)
print("multiply of elements in list is {}".format(x))


y=reduce((lambda s,t:s*t),l)
print("multiplication of elements in list by reduce() and lambda expression :", y)