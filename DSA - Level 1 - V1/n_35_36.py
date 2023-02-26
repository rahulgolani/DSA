'''
*
**   
***  
**** 
*****
'''

def printPattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end="")
        print()

if __name__ == '__main__':
    n=5
    printPattern(n)