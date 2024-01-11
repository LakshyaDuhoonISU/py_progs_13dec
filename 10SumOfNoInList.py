#wap function to sum all the numbers in a list
def add(a):
    sum=0
    for i in a:
        sum+=i
    print("Total sum:",sum)
a=[]
while True:
    b=int(input("Enter a number(0 to exit): "))
    if b==0:
        break
    else:
        a.append(b)
add(a)
