'''
0 
1 1
2 3 5
8 13 21 34
'''

def printPattern(n):
    a=0
    b=1
    for i in range(n):
        for _ in range(i+1):
            print(a,end=' ')
            c=a+b
            a=b
            b=c
        print()

if __name__ == '__main__':
    n=4
    printPattern(n)