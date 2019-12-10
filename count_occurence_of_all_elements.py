from collections import Counter
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

d=Counter(l)
print("elements occured times :",d)