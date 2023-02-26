# PRINT Z PATTERN
def printPattern(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                print('*',end='')
            else:
                if j==n-i-1:
                    print('*',end='')
                else:
                    print(' ',end='')
        print()
            

if __name__ == '__main__':
    n=5
    printPattern(n)