l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)

'''
x=[]
for i in range(len(l),0,-1):
    x.append(i)

print("list after reversing by copying values in a new list :",x) 
'''

'''
l.reverse()
print("list after reversing by reverse method :",l)
'''

print("list after reversing using slice operator :",l[::-1])