l=[]
z=int(input("enter the size of array :"))
for i in range(0,z):
 m=int(input("enter the element in array :"))
 l.append(m)

for i in range(0,len(l)):
    if l[i]<l[i+1] or l[i]>l[i+1]:
        print("true")

