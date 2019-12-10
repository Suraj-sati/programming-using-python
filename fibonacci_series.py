print("program for fibonacci series")
print()
num=int(input("how many numbers for  u want fibonacci series"))
print()
x=0
y=1
print("first number is :",     x)
print("second number is :",    y)
for i in range(0,num):
    sum=x+y
    t=x
    z=y
    x=y
    y=sum
    print("sum of {} and {} is :    {}".format(t,z,sum))
