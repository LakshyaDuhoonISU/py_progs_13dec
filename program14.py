#wap function that takes a list and returns a new list with distinct elements from first list
def distin(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
a=[]
while True:
    c=int(input("Enter a number(0 to exit): "))
    if c == 0:
        break
    else:
        a.append(c)
distin(a)
