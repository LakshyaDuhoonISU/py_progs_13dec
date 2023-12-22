#wap function to calculate factorial of a non negative number
def fact(a):
    if a<0:
        print("Negative number not accepted")
    elif a==1 or a==0:
        return 1
    else:
        return a*fact(a-1)
a=int(input("Enter a positive number: "))
c=fact(a)
print("Factorial of",a,"is",c)
