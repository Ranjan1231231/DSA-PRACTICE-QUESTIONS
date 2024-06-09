# Q)Given an array arr of distinct elements of size n, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

# arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

# Note: Modify the given arr[] only, If your transformation is correct, the output will be 1 else the output will be 0. 

# Examples

# Input: n = 7, arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: 3 7 4 8 2 6 1
# Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1
# Input: n = 4, arr[] = {1, 4, 3, 2}
# Output: 1 4 2 3
# Explanation: 1 < 4 > 2 < 3
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


# OPTIMISED CODE O(N)

from typing import List


class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        for i in range(n-1):
            if i %2==0:
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
            else:
                if arr[i]<arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
        return arr
#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":

    def isZigzag(n: int, arr: List[int]) -> bool:
        f = 1

        for i in range(1, n):
            if f:
                if arr[i - 1] > arr[i]:
                    return False
            else:
                if arr[i - 1] < arr[i]:
                    return False
            f = f ^ 1

        return True

    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        obj.zigZag(n, arr)
        check = True
        check = isZigzag(n, arr)
        if check:
            print("1")
        else:
            print("0")

# } Driver Code Ends
