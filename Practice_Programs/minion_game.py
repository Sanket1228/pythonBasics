def minion_game(string):
    vowel = 'AEIOU'
    kevsc = 0
    stusc = 0
    
    for i in range(len(string)):
        if string[i] in vowel:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin" , kevsc)
    elif stusc:
        print("stuart", stusc)
    else:
        print("Draw")

    



if __name__ == '__main__':
    s = input("Enter a string : ")
    minion_game(s)