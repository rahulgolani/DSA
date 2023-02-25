#ANY BASE TO DECIMAL

def convertToDecimal(num,base):
    power=1
    result=0
    while num>0:
        rem=num%10
        result+=(rem*power)
        power*=base
        num=num//10
    return result

if __name__ == '__main__':
    num=1172
    base=8
    result=convertToDecimal(num,base)
    print(f"{num} given in base {base} is {result} in decimal")