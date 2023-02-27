'''
Given a number n and n numbers in an array, print the bar chart corresponding to the values in the array

Example- n=5 arr=[3,1,0,7,5]

Output-

      *   
      *   
      * * 
      * * 
*     * * 
*     * * 
* *   * *
'''

def printBarChart(n,arr):
    nRows=max(arr)
    for i in range(nRows):
        for j in range(n):
            if nRows-arr[j]<=i:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

if __name__ == '__main__':
    n=5
    arr=[3,1,0,7,5]
    printBarChart(n,arr)