


def largest(x):
     h=l[0]
     for i in x:
          if i>h:
             h=i
     return h
l=[]
z=int(input("enter the size of array :"))
for i in range(0,z):
 m=int(input("enter the element in array :"))
 l.append(m)
print("largest element in array is ",largest(l))