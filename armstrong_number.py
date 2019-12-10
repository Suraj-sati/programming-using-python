print("program to check armstrong number")
print()
num=input("enter the number :")
l=len(num)
sum=0
for i in num:
    sum=sum+int(i)**l

if sum==int(num):
    print("it is armstrong")
else:
    print("not armstrong")
