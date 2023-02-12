def printPattern(n):
    for i in range(n):
        for _ in range(i):
            print(' ',end='')
        print('*',end='')
        print()

if __name__ == '__main__':
    n=5
    printPattern(n)