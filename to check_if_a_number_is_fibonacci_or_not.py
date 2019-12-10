print("to check a number is fibonacci or not ")
print()
x=0
y=1
sum=0
num=int(input("enter the number to check if it is fibonacci or not :"))
while sum<num:
    sum=x+y
    x=y
    y=sum


if num ==sum:
     print("yes ",num," is a fibonacci number")
else:
     print(num,"is not a fibonacci number")
    
