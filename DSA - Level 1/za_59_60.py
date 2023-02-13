from math import factorial

def calculateCombination(r,c):
    return factorial(r)//(factorial(c)*factorial(r-c))

def printPattern(n):
    for i in range(n):
        for j in range(i+1):
            print(calculateCombination(i,j),end=' ')
        print()

if __name__ == '__main__':
    n=6
    printPattern(n)