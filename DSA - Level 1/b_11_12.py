# CHECK IF NUMBER IS PRIME OR NOT
import math

def checkIfPrime(n):
    for i in range(2,math.floor(math.sqrt(n))):
        if n % i==0:
            return False
    return True

if __name__ == '__main__':
    t=int(input('Enter number of test cases'))
    for _ in range(t):
        n=int(input('Enter Number.'))
        print('Prime') if checkIfPrime(n) else print('Not Prime')