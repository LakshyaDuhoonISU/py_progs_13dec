#wap function to find maximum of three numbers
def maxi(a,b,c):
    if a<0 or b<0 or c<0:
        print("Enter negative numbers")
    else:
        print("Maximum of three numbers is:",max(a,b,c))
a=float(input("Enter a number: "))
b=float(input("Enter b number: "))
c=float(input("Enter c number: "))
maxi(a,b,c)
