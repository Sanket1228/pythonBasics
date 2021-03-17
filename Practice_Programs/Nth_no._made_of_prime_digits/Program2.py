def nthPrimeDigitsNumbers(number):
    num = " "
    while(number > 0):
        rem = number % 4
        if rem == 1:
            num += '2'
        if rem == 2:
            num += '3'
        if rem == 3:
            num += '5'
        if rem == 0:
            num += '7'
        if number % 4 == 0:
            number = number - 1
        number = number // 4
    return num[::-1]

number = 21;  
print(nthPrimeDigitsNumbers(10));  
print(nthPrimeDigitsNumbers(number));
