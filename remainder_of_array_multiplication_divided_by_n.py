
l=[]
z=int(input("enter the size of array :"))
for i in range(0,z):
 m=int(input("enter the element in array :"))
 l.append(m)
s=1
z=int(input("enter the digit from which u want to divide : "))
for i in range(0,len(l)):
    s=s*l[i]
print("multiplication of array elements is ",s)
print("remainder when array multiplication is divided by ",z,"is",s%z)
