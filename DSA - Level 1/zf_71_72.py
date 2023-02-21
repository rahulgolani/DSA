'''
* * * *     * 
      *     *
      *     *
* * * * * * *
*     *       
*     *
*     * * * *
'''

def printPattern(n):

    for i in range(n):
        for j in range(n):

            if i<n//2:
                if j==n//2 or (i==0 and j<n//2) or j==n-1:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            elif i==n//2:
                print('*',end=' ')
            else:
                if j==n//2 or (i==n-1 and j>n//2) or j==0:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')

        print()

if __name__ == '__main__':
    n=7
    printPattern(n)