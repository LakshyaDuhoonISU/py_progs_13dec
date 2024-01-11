#wap function to multiply all the numbers in a list
def multiple(a):
    multiplication=1
    for i in a:
        multiplication*=i
    print("Total multiplication:",multiplication)
a=[]
while True:
    b=int(input("Enter a number(0 to exit): "))
    if b==0:
        break
    else:
        a.append(b)
multiple(a)
