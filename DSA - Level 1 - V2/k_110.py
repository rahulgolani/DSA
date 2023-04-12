#FIND NEXT GREATER ELEMENT TO THE RIGHT

def findNextGreaterElement(arr):
    stack=[]
    nge=[None]*len(arr)
    stack.append(0)
    for i in range(1,len(arr)):
        while len(stack)>0 and arr[stack[-1]]<arr[i]:
            #Keep popping the smaller elements and make the current element answer of those
            nge[stack[-1]]=arr[i]
            stack.pop()
        # Push the current element
        stack.append(i)
    while len(stack):
        # The elements left have -1 as the answer
        nge[stack[-1]]=-1
        stack.pop()
    return nge

if __name__ == '__main__':
    arr=[2,5,9,3,1,12,6,8,7]
    nge=findNextGreaterElement(arr)
    print(arr)
    print(nge)