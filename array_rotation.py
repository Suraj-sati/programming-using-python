l=[]
z=int(input("enter the size of array :"))
for i in range(0,z):
 m=int(input("enter the element in array :"))
 l.append(m)

r=int(input("enter how many digits u want to rotate :"))
print("array before rotation",l)
print("array after rotation by ",r,"place")
l1=l[0:r]
l2=l[r:]
print(l2+l1)

