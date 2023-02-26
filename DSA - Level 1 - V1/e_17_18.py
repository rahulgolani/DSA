#COUNT NUMBER OF DIGITS IN A NUMBER

def getNumberOfDigits(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count

if __name__ == '__main__':
    n=934562
    print(getNumberOfDigits(n))