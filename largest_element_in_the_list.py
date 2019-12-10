
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)

x=l[0]
for i in l:
   if x<i:
    x,i=i,x
print("largest element in list is :",x)

print("largest element in list using max() function :",max(l))


l.sort()
print("largest element by sorting list in ascending order :",l[s-1])