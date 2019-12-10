l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

print("list before :",l)
l[0],l[-1]=l[-1],l[0]
print("list after interchanging first and last element : ",l)