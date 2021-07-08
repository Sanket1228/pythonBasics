class A:
    classvariable1 = "I'm classvariable A"

    def __init__(self):
        self.var1 = "I'm from class A constructor"
        self.classvariable1 = "I am I'm classvariable A in constructor"
        self.special = "special"

class B(A):
    classvariable1 = "I'm classvariable B"

    def __init__(self):
        self.var1 = "I'm from class A constructor"
        self.classvariable1 = "I am I'm classvariable B in constructor"
        super().__init__()
        print(super().classvariable1)

a = A()
b = B()

print(b.classvariable1,b.special)