#multilevel inheritance
class Grandfather:
    def __init__(self):
        self.name="ABC"
        self.inherit=10000
        self.purchase=1000
class Father(Grandfather):
    def __init__(self):
        super().__init__() #due to super().__init__ , the constructor from parent class is called in the child class as well
        self.name=" XYZ "+self.name #therefore all the values from right hand side are from the parent class using self.variable_name
        self.inherit=self.inherit #we don't need to write parent class name while accessing methods and attributes of it
        self.purchase=10000+self.purchase #as super().__init__ is used, we only need to write self.method_name or self.attribute
class Husband:
    def __init__(self):
        self.name=" John"
        self.inherit=100000
        self.purchase=50000
class Child(Father,Husband):
    def __init__(self,name):
        super().__init__()
        self.name=name+self.name
        self.inherit=self.inherit
        self.purchase=self.purchase
        print("Hello",self.name)
        print("Inherited property: Rs",self.inherit)
        print("Purchased property: Rs",self.purchase)
        print("Total property:",self.inherit+self.purchase)
obj=Child("Jane")
