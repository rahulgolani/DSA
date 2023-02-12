def printPattern(n):
    spaces=n-1
    for i in range(n):
        for _ in range(spaces):
            print(' ',end='')
        print('*',end='')
        spaces-=1
        print()

if __name__ == '__main__':
    n=5
    printPattern(n)