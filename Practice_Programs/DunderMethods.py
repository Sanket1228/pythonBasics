class A:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name

    def __add__(self, other):
        return self.salary + other.salary

    def __concat__(self, other):
        return self.name + other.name

    def __truediv__(self,other):
        return self.salary / other.salary


a = A(9000,'sanket')
b = A(10000,'ganesh')

print(a+b)
print(a+b)
print(a/b)
