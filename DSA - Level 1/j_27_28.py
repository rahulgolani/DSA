def getGCD(dividend,divisor):
    if divisor==0:
        return dividend

    return getGCD(divisor,dividend%divisor)


if __name__ == '__main__':
    a=60
    b=48
    print(getGCD(a,b))