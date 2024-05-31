# # QUESTION
# Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some integer x. Return true if N is power of 2 else return false.

# Example 1:

# Input: 
# N = 8
# Output: 
# YES
# Explanation:
# 8 is equal to 2 raised to 3 (23 = 8).
# Example 2:

# Input: 
# N = 98
# Output: 
# NO
# Explanation: 
# 98 cannot be obtained by any power of 2.
# Your Task:Your task is to complete the function isPowerofTwo() which takes n as a parameter and returns true or false by checking if the given number can be represented as a power of two or not.

# Expected Time Complexity:O(log N).
# Expected Auxiliary Space:O(1).

# NOT OPTIMIZED O(LOG 2 N)
        # i = 0
        # if n==0:
        #     return False
        # while True :
        #     if 2 ** i == n :
        #         return True
        #     if 2 ** i > n :
        #         return False
        #     i += 1


# OPTIMIZED O(1)

#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n : int ) -> bool:
        ##Your code here
        if n>0:
            # a number is power of two if bitwise "and" between n and n-1 is 0: 
            if (n&(n-1))==0:
                return True
        else:
            return False
        
        

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
