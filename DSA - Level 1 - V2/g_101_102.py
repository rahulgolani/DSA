'''
Given two arrays. Return an array containing the difference of two arrays
'''

def getDifference(n1,a1,n2,a2):
    
    diffArr=[]
    carry=0
    while n1>0 or carry>0:
        dig1=a1[n1-1]-carry if n1>0 else 0
        dig2=a2[n2-1] if n2>0 else 0
        dig=dig1+10-dig2 if dig1<dig2 else dig1-dig2
        carry=1 if dig1<dig2 else 0
        n1-=1
        n2-=1
        diffArr.insert(0,dig)
    return int(''.join(map(str,diffArr)))

if __name__ == '__main__':
    n1=int(input('Enter Size of Array 1'))
    a1=[]
    for _ in range(n1):
        a1.append(int(input()))
    
    n2=int(input('Enter Size of Array 2'))
    a2=[]
    for _ in range(n2):
        a2.append(int(input()))
    print(getDifference(n1,a1,n2,a2))
