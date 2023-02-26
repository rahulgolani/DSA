'''
*** ***
**   **
*     *
**   **
*** ***
'''

def printPattern(n):
    stars=(n//2)+1
    spaces=1
    for i in range(n):
        
        for _ in range(stars):
            print('*',end='')
        
        for _ in range(spaces):
            print(' ',end='')
        
        for _ in range(stars):
            print('*',end='')

        if i<n//2:
            stars-=1
            spaces+=2
        else:
            stars+=1
            spaces-=2

        print()

if __name__ == '__main__':
    n=5
    printPattern(n)