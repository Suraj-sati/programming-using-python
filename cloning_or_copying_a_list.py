
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

a=[]

a=l.copy()
print("list after copying from L list variable to A list variale by copy() method :",a)

b=[]
b=l[:]
print("copying list by slicing[:] technique :",b)

c=[]
c.extend(l)
print("copying list by extend() method : ",c)

d=[]
for i in l:
    d.append(i)
print("copying list by append() method :",d)

e=[]
e=list(l)
print("copyng list by list() method :",e)

f=[i for i in l]
print("list after copying using list comprehension :",f)

if(a==b==c==d==e):
    print("a==b==c==d==e==f==l becoz content of all list object is same")
