#wap function to reverse a string
'''def reversed(a):
    print(a[::-1])'''
def reversed(a):
    for i in range(len(a)):
        print(a[len(a)-i-1],end='')
a=input("Enter a string: ")
reversed(a)
