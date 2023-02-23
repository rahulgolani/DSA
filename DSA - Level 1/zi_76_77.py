def calculateDigitFrequency(num,n):
    count=0
    while num>0:
        digit=num%10
        if digit==n:
            count+=1
        num=num//10
    return count

if __name__ == '__main__':
    num=95439692
    n=9
    
    print(calculateDigitFrequency(num,n))