'''
*           * 
*           * 
*           * 
*     *     * 
*   *   *   * 
* *       * * 
*           *
'''

def printPattern(n):
    for i in range(n):
        for j in range(n):

            if i<n//2:
                if j==0 or j==n-1:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            elif i==n//2:
                if j==0 or j==n-1 or j==n//2:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            else:
                if j==0 or j==n-1 or (i+j==n-1) or (i==j):
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
        print()

if __name__ == '__main__':
    n=7
    printPattern(n)