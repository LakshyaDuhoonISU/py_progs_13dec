#single inheritance
'''class Parent:
    def add(a,b):
        print("Sum:",a+b)
class Child(Parent):
    def takevalue(self):
        c=float(input("Enter a number: "))
        d=float(input("Enter another number: "))
        Parent.add(c,d)
obj=Child()
obj.takevalue()'''

'''class Parent:
    def add(self,a,b):
        print(a[0]+a[1])
class Child(Parent):
    def takevalue(self):
        c=float(input("Enter a number: "))
        d=float(input("Enter another number: "))
        x=[c,d]
        return x
obj=Child()
e=obj.takevalue()
#print(e)
f=obj.add(e)'''

'''class Shape:
    def s_area(a):
        print("Area:",a*a)
    def c_area(a):
        print("Area:",3.14*a*a)
    def t_area(a,b):
        print("Area:",0.5*a*b)
class Circle(Shape):
    def takevalue(self):
        a=float(input("Enter radius: "))
        Shape.c_area(a)
class Square(Shape):
    def takevalue(self):
        a=float(input("Enter side: "))
        Shape.s_area(a)
class Triangle(Shape):
    def takevalue(self):
        a=float(input("Enter base: "))
        b=float(input("Enter height: "))
        Shape.t_area(a,b)
c=int(input("Select which area you want to find:\n1.Circle\n2.Square\n3.Triangle\n"))
if c==1:
    obj=Circle()
    obj.takevalue()
elif c==2:
    obj=Square()
    obj.takevalue()
elif c==3:
    obj=Triangle()
    obj.takevalue()
else:
    print("Invalid choice")'''

'''class Area: #program to overcome function overloading in python
    def area(self,a): #data structures should be used for large amounts of data
        if len(a)==1:
            print("Area of circle:",3.14*a[0]*a[0])
        elif len(a)==2:
            print("Area of rectangle:",a[0]*a[1])
class Value(Area):
    def takevalue(self):
        x=[]
        a=int(input("Which area do you want:\n1.Circle\n2.Rectangle\n"))
        if a==1:
            b=float(input("Enter radius: "))
            x.append(b)
            return x
        elif a==2:
            b=float(input("Enter length: "))
            c=float(input("Enter breadth: "))
            x+=[b,c]
            return x
obj=Value()
a=obj.takevalue()
obj.area(a)'''

class Area: #program to overcome function overloading in python
    def area(a,b): 
        if b==None:
            print("Area of circle:",3.14*a*a)
        elif a==None:
            print("Area of square:",b*b)
        else:
            print("Area of rectangle:",a*b)
    def __del__(self):
        print("Destructor is called")
class Value(Area):
    def takevalue(self):
        a=int(input("Which area do you want:\n1.Circle\n2.Square\n3.Rectangle\n"))
        if a==1:
            a=float(input("Enter radius: "))
            Area.area(a,None)
        elif a==2:
            b=float(input("Enter side: "))
            Area.area(None,b)
        elif a==3:
            b=float(input("Enter length: "))
            c=float(input("Enter breadth: "))
            Area.area(b,c)
obj=Value()
obj.takevalue()
del obj
