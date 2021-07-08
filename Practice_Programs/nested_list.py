if __name__ == '__main__':
    marksheet = []
    for _ in range(int(input("Enter number of students "))):
        marksheet.append([input("Enter name : "),float(input("Enter marks : "))])

    second_highest_number = sorted(list(set([marks for name, marks in marksheet])))[1]
    print([a for a,b in sorted(marksheet) if b == second_highest_number])
        