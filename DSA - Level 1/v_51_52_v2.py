'''
*   *
 * * 
  *  
 * * 
*   *
'''

def printPattern(n):
    k=n-1
    for i in range(n):
        for j in range(n):
            if j==i:
                print('*',end='')
            elif j==k:
                print('*',end='')
            else:
                print(' ',end='')
        print()
        k-=1

if __name__ == '__main__':
    n=5
    printPattern(n)