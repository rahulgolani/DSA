'''
*******
 *   * 
  * *  
   *   
  ***  
 ***** 
*******
'''

def printPattern(n):
    outerSpace=1
    innerSpace=n-4
    for i in range(n//2):
        if i==0:
            for _ in range(n):
                print('*',end='')
        else:
            for _ in range(outerSpace):
                print(' ',end='')
            print('*',end='')
            for _ in range(innerSpace):
                print(' ',end='')
            print('*',end='')
            outerSpace+=1
            innerSpace-=2
        print()
    stars=1
    spaces=n//2
    for i in range(n//2,n):
        # if i==n-1:
        #     for _ in range(n):
        #         print('*',end='')
        for _ in range(spaces):
            print(' ',end='')
        for _ in range(stars):
            print('*',end='')
        stars+=2
        spaces-=1
        
        
        
        print()


if __name__ == '__main__':
    n=7
    printPattern(n)