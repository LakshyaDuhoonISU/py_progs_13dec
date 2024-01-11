#class object in python
class Student:
    count=0 #count is a class variable(it is common for every object)
    def __init__(self,name,age): #self is a pointer which is used to tell the compiler to change variables of only that one object and not make changes in every object created
        self.name=name #constructor is invoked
        self.age=age
        Student.count+=1 #class variable is accessed using class_name.data_member 
        print("Constructor is called")
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
obj=Student("ABC",18)
obj.display()
obj1=Student("XYZ",30)
obj1.display()
print("Total objects created:",Student.count) 
