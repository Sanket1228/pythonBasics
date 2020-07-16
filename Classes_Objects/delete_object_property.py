class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello my name is",self.name)

p = MyClass("Sanket",20)
del p.age

print(p.age)            #this will produce error because "age" property is already deleted