#SPAN OF AN ARRAY
'''
Given a number n and n numbers, find the difference between the highest and lowest numbers.

Array - Sorted ? - O(1)
Array - Rotated-Sorted ? - O(logn)
Array - Random ? - O(n)
'''

import math

def findSpan(arr,n):
    max=-math.inf
    min=math.inf
    for i in range(n):
        if arr[i]>max:
            max=arr[i]
        if arr[i]<min:
            min=arr[i]
    return max-min


if __name__ == '__main__':
    n=5
    arr=[1,2,3,4,5]
    result=findSpan(arr,n)
    print(result)