def findNGER(arr,n,nge,stack):
    for i in range(n-1,-1,-1):
        while len(stack)>0 and arr[i]>arr[stack[-1]]:
            stack.pop()
        if len(stack)==0:
            nge[i]=n
        else:
            nge[i]=stack[-1]
        stack.append(i)

def findMaxOfWindow(arr,n,k):
    nge=[None]*n
    stack=[]
    findNGER(arr,n,nge,stack)
    # print(nge)
    # j=0
    for i in range(n-k+1):
        j=i
        # if j<i:
        #     j=i
        while nge[j]<(i+k):
            j=nge[j]
        print(arr[j],end=' ')
    
if __name__ == '__main__':
    arr=[2,9,3,8,1,7,12,6,14,4,32,0,7,19,8,12,6]
    k=4
    findMaxOfWindow(arr,len(arr),k)