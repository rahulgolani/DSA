#PRINT DIGITS OF A NUMBER FROM LEFT TO RIGHT

def getDigitsOfaNumber(n):
    digits=[]
    while n>0:
        digit=n%10
        digits.append(digit)
        n=n//10
    for i in range(len(digits)-1,-1,-1):
        print(digits[i])

if __name__ == '__main__':
    n=665784783
    getDigitsOfaNumber(n)