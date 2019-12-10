l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=input("enter the element in list:")
    l.append(m)
print("list brefore :",l)


l.clear()
print("list after clearing using clear method :",l)


'''
for i in range(0,s-1):
    l.remove(l[i])
print("list after removing all element by remove method :",l)
'''

for i in range(0,len(l)):
    l.pop()
print("list after removing element by pop() method :",l)

for i in range(0,len(l)):
    l[i]=""
print("list after reassigning blank :",l)

l*=0
print("list after multiplying by 0 :",l)


del l[:]
print("list after deleting all elements :",l)
