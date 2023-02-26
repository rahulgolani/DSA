#FIBONACCI NUMBERS TILL N

def getFibonacciNumbers(n):
    fibA=0
    fibB=1
    count=2
    print(fibA)
    print(fibB)
    while count<n:
        fibC=fibA+fibB
        fibA=fibB
        fibB=fibC
        print(fibC)
        count+=1


if __name__ == '__main__':
    n=10
    getFibonacciNumbers(n)