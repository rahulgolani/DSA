'''
Given two arrays. Return an array containing the sum of two arrays
'''

def getSumOfTwoArrays(n1,a1,n2,a2):
    sumArr=[]
    carry=0
    while n1>0 or n2>0 or carry>0:
        dig1=a1[n1-1] if n1>0 else 0
        dig2=a2[n2-1] if n2>0 else 0
        dig=dig1+dig2+carry
        carry=dig//10 if dig>=10 else 0
        dig=dig%10 if dig>=10 else dig
        sumArr.insert(0,dig)
        n1-=1
        n2-=1
    return sumArr

if __name__ == '__main__':
    n1=5
    n2=6
    a1=[3,1,0,7,5]
    a2=[1,1,1,1,1,1]
    result=getSumOfTwoArrays(n1,a1,n2,a2)
    print(result)
    

    n1=4
    n2=6
    a1=[9,9,9,9]
    a2=[9,9,9,9,9,9]
    result=getSumOfTwoArrays(n1,a1,n2,a2)
    print(result)