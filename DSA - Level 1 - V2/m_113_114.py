def findNextSmallerElementLeft(arr,n,nsel):
    stack=[]
    for i in range(n):
        while len(stack)>0 and arr[i]<arr[stack[-1]]:
            stack.pop()
        if len(stack)>0:
            nsel[i]=stack[-1]
        else:
            nsel[i]=-1
            # nsel[i]=0
        stack.append(i)

def findNextSmallerElementRight(arr,n,nser):
    stack=[]
    for i in range(n-1,-1,-1):
        while len(stack)>0 and arr[i]<arr[stack[-1]]:
            stack.pop()
        if len(stack)>0:
            nser[i]=stack[-1]
        else:
            # nser[i]=-1
            nser[i]=n
        stack.append(i)

def findLargestAreaHistogram(arr,n):
    nsel=[None]*len(arr)
    nser=[None]*len(arr)
    findNextSmallerElementLeft(arr,n,nsel)
    findNextSmallerElementRight(arr,n,nser)
    largestArea=float('-infinity')
    for i in range(n):
        # area=0
        # if nser[i]==-1:
        #     area+=(n-i)*arr[i]
        # else:
        #     area+=(nser[i]-i)*arr[i]
        # if nsel[i]==-1:
        #     area+=(i)*arr[i]
        # else:
        #     area+=(i-nsel[i]-1)*arr[i]
        area=(nser[i]-nsel[i]-1)*arr[i]
        largestArea=max(area,largestArea)
    return largestArea


if __name__ == '__main__':
    arr=[6,2,5,4,5,1,6]
    n=7
    print(findLargestAreaHistogram(arr,n))