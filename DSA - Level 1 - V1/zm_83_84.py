#ANY BASE TO ANY BASE

def convertToDecimal(num,iBase):
    power=1
    result=0
    while num>0:
        rem=num%10
        result+=rem*power
        power*=iBase
        num=num//10
    return result

def convertToAnyBase(num,oBase):
    power=1
    result=0
    while num>0:
        rem=num%oBase
        result+=rem*power
        power*=10
        num=num//oBase
    return result

def convertAnyToAnyBase(num,iBase,oBase):
    temp=convertToDecimal(num,iBase)
    result=convertToAnyBase(temp,oBase)
    return result

if __name__ == '__main__':
    num=1172
    b1=8
    b2=9
    result=convertAnyToAnyBase(num,b1,b2)
    print(f"{num} in given base {b1} is {result} in {b2} base")
