
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)

sum=0
for i in l:
    sum=sum+i
print("sum of elements in list is {}".format(sum))
print(type(l))

'''
t=sum(l)
print("sum of elements of list by sum() function :",t)
'''