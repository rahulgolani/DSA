'''
    *
   **
  ***
 ****
*****
'''

def printPattern(n):
    spaces=n-1
    stars=1
    for i in range(n):
        for _ in range(spaces):
            print(' ',end='')
        for _ in range(stars):
            print('*',end='')
        spaces-=1
        stars+=1
        print()

if __name__ == '__main__':
    n=5
    printPattern(n)