l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m.strip())

x=input("enter the element u want to check :")
x=x.strip()
if x in l:
    print("yes", x ," is in list")
else:
    print(x,"is not in list")


for i in range(0,len(l)):
    if l[i]==x:
        print("yes its in list")
        break
else:
    print("not in list")

