
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)
c=0
d=0
for i in l:
   if i%2==0:
       c+=1
   else:
       d+=1

print("total even number in list are :",c)
print("total odd number in list are :",d)