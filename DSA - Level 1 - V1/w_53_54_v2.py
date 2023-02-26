'''
  *  
 * * 
*   *
 * * 
  *  

INNER SPACE OUTER SPACE CONCEPT
'''


def printPattern(n):
    outerSpace=n//2
    innerSpace=-1
    for i in range(n):
        for _ in range(outerSpace):
            print(' ',end='')
        print('*',end='')
        if innerSpace>0:
            for _ in range(innerSpace):
                print(' ',end='')
            print('*',end='')
        print()
        if i<n//2:
            outerSpace-=1
            innerSpace+=2
        else:
            outerSpace+=1
            innerSpace-=2

if __name__ == '__main__':
    n=5
    printPattern(n)