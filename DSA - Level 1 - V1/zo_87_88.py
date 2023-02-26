def baseSubtraction(n1,n2,base):
    power=1
    result=0
    carry=0
    while n2>0 or n1>0 or carry>0:
        dig2=n2%10-carry if n2>0 else 0
        dig1=n1%10 if n1>0 else 0
        dig=base+dig2-dig1 if dig2<dig1 else dig2-dig1
        carry=1 if dig2<dig1 else 0
        result+=dig*power
        power*=10
        n1=n1//10
        n2=n2//10
    return result

if __name__ == '__main__':
    n2=1212
    n1=236
    base=8
    result=baseSubtraction(n1,n2,base)
    print(f"{n2} - {n1} in base {base} is {result}")