#INVERSE OF A NUMBER

# Digits acts as Index
# Index acts as Digits

def inverseNumber(num):
    inversedNumber=0
    count=1
    while num>0:
        digit=num%10
        inversedNumber+= ((10**(digit-1))*count)
        num=num//10
        count+=1
    return inversedNumber

if __name__ == '__main__':
    num=15234
    print(inverseNumber(num))