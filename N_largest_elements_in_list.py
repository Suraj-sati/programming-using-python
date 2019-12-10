
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)

x=int(input("enter how many largest elements u want :"))
l.sort()
print("list is :",l)
print("largest",x,"elements by sorting  are :",l[len(l)-x:])

l.sort()
z=[]
for i in range(x):
    z.append(max(l))
    l.remove(max(l))
z.sort()
print("largest",x,"elements by adding max element to an empty list and removing last element are :",z)
