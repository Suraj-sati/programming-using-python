l=[]
z=int(input("enter the size of list:"))
for i in range(0,z):
 m=int(input("enter the element in list :"))
 l.append(m)
print()
x=int(input("enter the element to swap : "))
y=int(input("enter element to whom u have to swap : "))
c=0
d=0
print("list before swapping ",l)
for i in l:
    if x==i:
        e=c
    else:
        c+=1
    if y==i:
        f=d
    else:
        d+=1

l[e],l[f]=l[f],l[e]
print("list after swapping elements",l)
