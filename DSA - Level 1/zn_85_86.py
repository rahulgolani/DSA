#ADD TWO NUMBERS THE GIVEN BASE

def baseAddition(n1,n2,base):
    carry=0
    power=1
    result=0
    while n1>0 or n2>0 or carry>0:
        dig1=n1%10 if n1>0 else 0
        dig2=n2%10 if n2>0 else 0
        dig=dig1+dig2+carry
        carry=dig//base if dig>=base else 0
        dig=dig%base if dig>=base else dig
        result+=dig*power
        power*=10
        n1=n1//10
        n2=n2//10
    return result


if __name__ == '__main__':
    n1=234
    n2=444
    base=5
    result=baseAddition(n1,n2,base)
    print(f"{n1} + {n2} in base {base} is {result}")
    n1=236
    n2=754
    base=8
    result=baseAddition(n1,n2,base)
    print(f"{n1} + {n2} in base {base} is {result}")