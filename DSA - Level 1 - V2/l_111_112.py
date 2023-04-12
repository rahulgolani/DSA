def findStockSpan(arr,n):
    stack=[]
    stockSpan=[0]*len(arr)
    stack.append(0)
    stockSpan[0]=1
    for i in range(1,len(arr)):
        while len(stack)>0 and arr[i]>arr[stack[-1]]:
            stack.pop()
        if len(stack)>0:
            stockSpan[i]=i-stack[-1]
        else:
            stockSpan[i]=i+1
        stack.append(i)
    return stockSpan

if __name__ == '__main__':
    n=9
    arr=[2,5,9,3,1,12,6,8,7]
    result=findStockSpan(arr,n)
    print(arr)
    print(result)