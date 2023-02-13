'''
  *  
 * * 
*   *
 * * 
  *  
'''

def printPattern(n):
    star1=n//2
    star2=n//2
    for i in range(n):
        for j in range(n):
            if j==star1 or j==star2:
                print('*',end='')
            else:
                print(' ',end='')
        if i<n//2:
            star1-=1
            star2+=1
        else:
            star1+=1
            star2-=1
        print()


if __name__ == '__main__':
    n=5
    printPattern(n)