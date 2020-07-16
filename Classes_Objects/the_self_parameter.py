class MyClass:
    def __init__(myVariables,name,age):
        myVariables.name = name
        myVariables.age = age

    def my_function(abc):
        print("Hello my name is ",abc.name)

p = MyClass("Sanket",20)
p.my_function()