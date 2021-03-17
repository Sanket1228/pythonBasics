d = {1:'2',2:'3',3:'5',0:'7'}
num = " "
n = int(input("Enter the number : "))
while n>0:
    r = n%4
    num = d[r]+num
    n = n - 1
    n = int(n/4)
print(int(num))