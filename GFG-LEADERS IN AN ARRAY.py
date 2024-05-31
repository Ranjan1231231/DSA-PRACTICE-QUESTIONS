# QUESTION
# Given an array A of positive integers. Your task is to find the leaders in the array. An element of the array is a leader if it is greater than all the elements to its right side or if it is equal to the maximum element on its right side. The rightmost element is always a leader. 

# Example 1:

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 
# included.
# Example 2:

# Input:
# n = 5
# A[] = {10,4,2,4,1}
# Output: 10 4 4 1
# Explanation: 1 is the rightmost element and 4 is the element which is greater
# than all the elements to its right. Similarly another 4 is the element that is equal to the greatest element to its right and 10 is the greatest element in the whole array.
# Your Task:
# You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

# OPTIMISED SOLUTION O(N)
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        B=[]
        # select from right most element and set it as an leader as no number is after that, and add it to B
        max=A[-1]
        B.append(A[-1])
        #we will transverse from right and set a number max if it is greater than than the previous max also it is an leader
        for i in range(N-2,-1,-1):
            if A[i]>=max:
                max=A[i]
                B.append(A[i])
        # since we are looking through right we have to reverse the array as we have entered the leaders from right.
        B.reverse()
        return B
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
