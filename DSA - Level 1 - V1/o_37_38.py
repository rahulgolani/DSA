'''
*****
****
***
**
*
'''

def printPattern(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end='')
        print()

if __name__ == '__main__':
    n=5
    printPattern(n)