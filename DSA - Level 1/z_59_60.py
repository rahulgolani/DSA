'''
1       
1 1     
1 2 1   
1 3 3 1 
1 4 6 4 1   
1 5 10 10 5 1 
'''

def printPattern(n):
    matrix=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][0]=1
    for i in range(1,n):
        for j in range(1,i+1):
            if j==i:
                matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(matrix[i][j],end=' ')
        print()


if __name__ == '__main__':
    n=6
    printPattern(n)