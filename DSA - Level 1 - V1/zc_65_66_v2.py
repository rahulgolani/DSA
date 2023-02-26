'''
1     1
12   21
123 321
1234321
'''

def printPatternStars(n):
    stars=1
    spaces=2*n-3
    for i in range(n):
        for _ in range(stars):
            print('*',end='')
        
        for _ in range(spaces):
            print(' ',end='')
        
        if i==n-1:
            stars-=1

        for _ in range(stars):
            print('*',end='')
        
        stars+=1
        spaces=max(0,spaces-2)
        print()


def printPatternValues(n):
    stars=1
    spaces=2*n-3
    for i in range(n):
        value=1
        for _ in range(stars):
            print(value,end='')
        
        for _ in range(spaces):
            print(' ',end='')
        
        if i==n-1:
            stars-=1

        for _ in range(stars):
            print(value,end='')
        
        stars+=1
        spaces=max(0,spaces-2)
        print()

def printPattern(n):
    stars=1
    spaces=2*n-3
    for i in range(n):
        value=1
        for _ in range(stars):
            print(value,end='')
            value+=1
        
        for _ in range(spaces):
            print(' ',end='')
        
        if i==n-1:
            stars-=1
            value-=1

        for _ in range(stars):
            value-=1
            print(value,end='')
        
        stars+=1
        spaces=max(0,spaces-2)
        print()

if __name__ == '__main__':
    n=4
    # printPatternStars(n)
    # printPatternValues(n)
    printPattern(n)