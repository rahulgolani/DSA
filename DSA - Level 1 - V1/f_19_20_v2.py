#PRINT DIGITS OF A NUMBER FROM LEFT TO RIGHT WITHOUT USING SPACE 

def countDigits(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count

def getDigitsOfaNumber(n):
    numOfDigits=countDigits(n)
    divisor=10**(numOfDigits-1)
    while n>0:
        digit=n//divisor
        print(digit)
        n=n%divisor
        divisor=divisor//10

if __name__ == '__main__':
    n=665784783
    getDigitsOfaNumber(n)