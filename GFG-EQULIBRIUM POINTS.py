# QUESTION
# Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 
# 3 
# Explanation:  
# equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2). 
# Example 2:

# Input:
# n = 1
# A[] = {1}
# Output: 
# 1
# Explanation:
# Since there's only element hence its only the equilibrium point.
# Your Task:
# The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium. 

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


# UNOPTIMIZED CODE O(N^2)
        # if N==1:
        #     return 1
        # # Your code here
        # for i in range(0,N):
        #     if sum(A[0:i])==sum(A[i+1:N]):
        #         return i+1
        # return -1


# OPTIMISED CODE O(N)
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if N==1:
            return 1

        
        rightsum=sum(A)
        leftsum=0
        for i in range(N):
            rightsum-=A[i]
            if rightsum==leftsum:
                return i+1
            leftsum+=A[i]
        return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
        return -1
