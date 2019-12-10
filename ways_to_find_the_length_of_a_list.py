l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

print("length of list using len() function :",len(l))
print()

c=0
for i in l:
    c+=1
print("length of list by incrementing count variable is ",c)

