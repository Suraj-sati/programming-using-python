print("to check prime or not")
print()

num=int(input("enter the number to check prime or not  :"))
c=0
if num>1:
 for i in range(2,num):
    if num%i==0:
       c+=1
 if c>1:
    print("{} is not prime".format(num))
 else:
    print("{} is prime".format(num))
else:
    print("{} is not prime".format(num))
