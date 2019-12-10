
l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)

print("even number in list are : ")
for i in l:
    if i%2==0:
      print(i)
print("odd number in list are ")
for i in l:
    if i%2!=0:
      print(i)