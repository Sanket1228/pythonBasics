def factorial(n):
    yield factorial(n-1) 

fact = factorial(5)

print(fact)
print(fact.__next__())