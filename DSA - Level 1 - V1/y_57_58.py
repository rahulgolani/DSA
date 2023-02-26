'''
0 
1 1
2 3 5
8 13 21 34
'''

def printPattern(n):
    a=0
    b=1
    count=1
    for i in range(n):
        for j in range(i+1):
            if count==1:
                print(0,end=' ')
            elif count==2:
                print(1,end=' ')        
            else:
                c=a+b
                a=b
                b=c
                print(c,end=' ')
            count+=1
        print()
            

if __name__ == '__main__':
    n=5
    printPattern(n)