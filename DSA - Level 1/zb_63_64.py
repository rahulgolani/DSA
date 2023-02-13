'''
  1  
 232 
34543
 232 
  1  
'''

def printPattern(n):
    spaces=n//2
    stars=1
    value=1
    for i in range(n):
        j=0
        for _ in range(spaces):
            print(' ',end='')
            j+=1
        k=value
        for _ in range(stars):
            print(k,end='')
            
            # print('*',end='')
            if j<n//2:
                k+=1
            else:
                k-=1
            j+=1
        if i<n//2:
            spaces-=1
            stars+=2
            value+=1
        else:
            spaces+=1
            stars-=2
            value-=1
        print()

if __name__ == '__main__':
    n=5
    printPattern(n)