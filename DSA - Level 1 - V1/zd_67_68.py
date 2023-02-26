def printPattern(n):
    stars=1
    spaces=n//2
    for i in range(n):

        for _ in range(spaces):
            if i==n//2:
                print('*',end=' ')
            else:
                print(' ',end=' ')

        for _ in range(stars):
            print('*',end=' ')
        if i<n//2:
            stars+=1
        else:
            stars-=1
        print()

if __name__ == '__main__':
    n=15
    printPattern(n)