# CONVERT A DECIMAL NUMBER TO THE GIVEN BASE 

def convertToBase(num,base):
    result=0
    power=0
    while num>0:
        rem=num%base
        result+=(rem*(10**power))
        num=num//base
        power+=1
    return result

if __name__ == '__main__':
    num=634
    # base=8
    # base=9
    base=12
    result=convertToBase(num,base)
    print(f"{num} in base {base} is {result}")