'''
  *  
 ***
*****
 ***
  *
'''

def printPattern(n):
    start=n//2
    end=(n//2)+1
    for i in range(n):
        for _ in range(start):
            print(' ',end='')
        for _ in range(start,end):
            print('*',end='')
        for _ in range(end,n):
            print(' ',end='')
        if i<n//2:
            start-=1
            end+=1
        else:
            start+=1
            end-=1
        print()


if __name__ == '__main__':
    n=5
    printPattern(n)