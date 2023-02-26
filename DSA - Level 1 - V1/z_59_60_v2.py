'''
1
1 1
1 2 1
1 3 3 1       
1 4 6 4 1     
1 5 10 10 5 1
'''

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