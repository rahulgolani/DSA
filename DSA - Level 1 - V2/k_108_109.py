def findNextGreaterElement(arr):
    stack=[]
    nge=[None]*(len(arr))
    for i in range(len(arr)-1,-1,-1):
        while len(stack)>0 and stack[-1]<arr[i]:
            stack.pop()
        if len(stack)>0:
            nge[i]=stack[-1]
        else:
            nge[i]=-1
        stack.append(arr[i])
    return nge

if __name__ == '__main__':
    arr=[2,5,9,3,1,12,6,8,7]
    nge=findNextGreaterElement(arr)
    print(arr)
    print(nge)