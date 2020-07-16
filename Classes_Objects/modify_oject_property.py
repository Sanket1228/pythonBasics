class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello my name is",self.name)

p = MyClass("Sanket",20)
print(p.age)
p.age = 30
print(p.age)