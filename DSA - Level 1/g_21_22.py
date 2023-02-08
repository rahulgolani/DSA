#PRINT DIGITS OF A NUMBER IN REVERSE ORDER

def getDigitsReversed(num):
    while num>0:
        digit=num%10
        print(digit)
        num=num//10

if __name__ == '__main__':
    num=665784783
    getDigitsReversed(num)