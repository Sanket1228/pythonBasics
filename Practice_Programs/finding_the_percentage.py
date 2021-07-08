if __name__ == '__main__':
    n = int(input("Enter the number of student : "))
    my_dict = {}
    for _ in range(n):
        name, *mark = input("Enter name and marks : ").split()
        marks = list(map(float,mark))
        my_dict[name] = marks

    query_name = input("Enter query name : ")
    total_marks = sum(my_dict[query_name])
    average = total_marks/3
    print("%.2f"%(average))
