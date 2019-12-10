print("to find N'th fibonacci number")
print()
x=0
y=1
num=int(input("enter the position u want fibonacci number"))
for i in range(0,num):
    sum=x+y
    x=y
    y=sum
print("fibonacci number at {} position is {}".format(num,sum))
