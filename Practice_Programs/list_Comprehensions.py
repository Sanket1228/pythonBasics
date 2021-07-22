lst = []
n = int(input("Enter the number of values you want to enter : "))

for i in range(n):
    lst.append(i)

print("1 : List Comprehension , 2 : Set Comprehension, 3: Dictionary comprehension ")
choice = int(input("Which type of comprehension you want to use?"))

if(choice == 1):
    user_input = [i for i in lst]
    print(user_input)
elif(choice == 2):
    user_input = {i for i in lst}
    print(user_input)
elif(choice == 3):
    user_input = {i: f"Item {i}" for i in range(len(lst))}
    print(user_input)