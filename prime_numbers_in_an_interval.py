'''
print("prime numbers in an interval")
print()

num1=int(input("from where u want to get prime number :"))
num2=int(input("upto where u want to get prime number :"))
c=0
for i in range(num1,num2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
          print(i)

    
'''

num1=int(input("from where u want to get prime number :"))
num2=int(input("upto where u want to get prime number :"))
c=0
for i in range(num1,num2):
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
         print(i)
        
