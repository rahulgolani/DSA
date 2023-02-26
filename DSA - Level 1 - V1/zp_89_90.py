def baseAddition(n1,n2,base):
    result=0
    power=1
    carry=0
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

def baseMultiplication(n1,n2,base):
    oPower=1
    result=0
    while n2>0:
        iPower=oPower
        tempResult=0
        d=n2%10
        carry=0
        num=n1
        while num>0 or carry>0:
            m=num%10 if num>0 else 0
            dig=m*d+carry
            carry=dig//base if dig>=base else 0
            dig=dig%base if dig>=base else dig
            tempResult+=dig*iPower
            iPower*=10
            num=num//10
        result=baseAddition(result,tempResult,base)
        oPower*=10
        n2=n2//10
    return result

if __name__ == '__main__':
    n1=2156
    n2=74
    base=8
    result=baseMultiplication(n1,n2,base)
    print(f"{n1} * {n2} in base {base} is {result}")
    n1=234
    n2=76
    base=8
    result=baseMultiplication(n1,n2,base)
    print(f"{n1} * {n2} in base {base} is {result}")