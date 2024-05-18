class MyClass:
    class_variable = 0   # Class Variables

    def __init__(self, name):
        self.name = name  # Instance Variables
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)

    def print_name(self):
        print(self.name)
        

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2

obj1.print_name() 
obj2.print_name()