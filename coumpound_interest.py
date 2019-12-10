print("this is compound interest program")
print()

p=eval(input("enter pricipal amount :"))
r=eval(input("enter rate per annum (in %):"))
t=eval(input("enter time (in years) :"))

a=p*(1+(r/100))**t
print("interest :",a)
