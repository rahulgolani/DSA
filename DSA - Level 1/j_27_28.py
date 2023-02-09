#FIND GCD AND LCM using EUCLIDEAN ALGORITHM

def getGCD(dividend,divisor):
    if divisor==0:
        return dividend

    return getGCD(divisor,dividend%divisor)


if __name__ == '__main__':
    a=60
    b=48
    gcd=getGCD(a,b)
    print(gcd)
    lcm=(a*b)//gcd
    print(lcm)