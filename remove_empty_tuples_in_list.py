
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

t=list(filter(None,l))
print ("list after removing empty elements :",t)