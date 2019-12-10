l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

z=input("enter the element to want to remove :")
x=int(input("enter the time u want to remove its occurence :"))
for i in l:
   if(x==-1):
      print(i)
      break

   else:
       if z==i:
        x-=1
        l.remove(z)

print("list after removing multiple",z," :",l)