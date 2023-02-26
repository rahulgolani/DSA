#PRIME FACTORIZATION OF A NUMBER

from math import sqrt
from math import floor
def getPrimeFactors(num):
    for div in range(2,floor(sqrt(num))):
        while num%div==0:
            print(div,end=' ')
            num=num//div
    if num!=1:
        print(num)


if __name__ == '__main__':
    num=1440
    getPrimeFactors(num)