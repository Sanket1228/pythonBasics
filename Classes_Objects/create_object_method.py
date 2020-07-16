class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myFunction(self):
        print("Hello my name is ", self.name)

p = MyClass("Sanket",20)
p.myFunction()
    