
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)

z=int(input("enter from where u want even numbers :"))
y=int(input("enter upto where u want even numbers :"))
l.sort()
print("even numbers between",z,"and",y," are :")
for i in l:
    if i in range(z+1,y):
        if i%2==0:
            print(i)
print("odd number between",z,"and",y,"are ")
for i in l:
    if i in range(z+1,y):
        if i%2!=0:
            print(i)