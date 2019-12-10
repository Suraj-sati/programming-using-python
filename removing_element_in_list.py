from functools import reduce
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)


x=int(input("elements u want to remove :"))
for i in range(0,len(l)):
 if x in l:
   l.remove(x)

print("list after removing ",x,":",l)