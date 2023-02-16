'''
1     1
12   21
123 321
1234321
'''

def printPattern(n):
    totalCols=(2*n)-1
    spaces=totalCols-2
    # print(totalCols)
    # print(spaces)
    for i in range(n):
        value=1
        col=0
        # print(f'spaces -> {spaces}')
        for _ in range(i+1):
            print(value,end='')
            if col<totalCols//2:
                value+=1
            else:
                value-=1
            col+=1
            # value+=1
        # print(spaces)
        for _ in range(spaces):
            print(' ',end='')
            if col<totalCols//2:
                value+=1
            else:
                value-=1
            col+=1

        for _ in range(col,totalCols):
            print(value,end='')
            value-=1

        spaces=max(0,spaces-2)
        
        print()

if __name__ == '__main__':
    n=4
    printPattern(n)