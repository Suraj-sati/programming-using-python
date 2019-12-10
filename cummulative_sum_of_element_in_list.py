l=[]
s=int(input("enter the size of list :"))
for i in range(0,s):
    m=int(input("enter the element in list:"))
    l.append(m)
print("element in list are : ",end=" ")
for i in l:
    print(i,end="  ")
print()
print("cummulative sum is  : ",end=" ")
sum=l[0]
print(sum,end=" ")
for i in range(0,len(l)-1):
    sum=sum+l[i+1]
    print(sum,end="  ")

