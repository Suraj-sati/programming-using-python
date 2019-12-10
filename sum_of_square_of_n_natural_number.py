print("sum of square of N natural number")
print()
sum=0
num=int(input("enter the number upto u want to print sum of square of number :"))
for i in range(1,num+1):
    sum=sum+(i**2)
print("sum of square of first {} (1 to {}) natural numbers is {}".format(i,num,sum))
    
