from collections import Counter
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

x=input("enter the element to count its occurence :")

print("element",x," occured",l.count(x),"times")

c=0
for i in l:
    if x==i:
        c+=1
print("element",x,"occured",c,"times")


d=Counter(l)
print("element {} occured {}  times ".format(x,d[x]))
