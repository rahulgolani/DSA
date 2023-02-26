'''
1
1 1
1 2 1
1 3 3 1       
1 4 6 4 1     
1 5 10 10 5 1
'''

def printPattern(n):
    for i in range(n):
        val=1
        for j in range(i+1):
            print(val,end=' ')
            newVal=(val*(i-j))//(j+1)
            val=newVal
        print()

if __name__ == '__main__':
    n=6
    printPattern(n)