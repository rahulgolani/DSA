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
    stars=n
    spaces=0
    for i in range(n):
        for _ in range(spaces):
            print(' ',end='')
        for j in range(stars):
            if i>0 and i<n//2 and j>0 and j<stars-1:
                print(' ',end='')
            else:
                print('*',end='')
        print()
        if i<n//2:
            spaces+=1
            stars-=2
        else:
            stars+=2
            spaces-=1
            

if __name__ == '__main__':
    n=7
    printPattern(n)