def countDigits(num):
    count=0
    while num>0:
        count+=1
        num=num//10
    return count

def rotateNumber(num,k):
    numDigits=countDigits(num)
    k=k%numDigits if k>0 else numDigits+k #handle negative rotation(left)
    rem=num%(10**k)
    quo=num//(10**k)
    rotatedNumber=0
    rotatedNumber+=(rem*(10**(numDigits-k)))+(quo)
    return rotatedNumber

if __name__ == '__main__':
    num=21734
    # num=1234567
    k=9
    print(rotateNumber(num,k))