x=[]
n=int(input("enter the size of array :"))
sum=0
for i in range(0,n):
    m=eval(input("enter the element in array :"))
    x.append(m)
for i in x:
    sum=sum+i
print("sum of element of array is ",sum)
