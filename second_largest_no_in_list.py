
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)

x=l[0]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("second largest element by loop :",l[1])


l.sort()
print("second largest element by sorting list in ascending order :",l[s-2])


l.remove(max(l))
print("second largest element by removing largest element :",l[-1])