# PROBLEM STATEMENT
# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# Example 1:

# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.
# Example 2:

# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)


# MY INITIAL CODE
# class Solution:
#     #Function to find the sum of contiguous subarray with maximum sum.
#     def maxSubArraySum(self,arr,N):
#         result=[]

#         #TO GO THROUGH CONSUCUTIVE SUBSETS IN THE ARRAY
#         for i in range(N+1):
#             for j in range(i+1,N+1):#i+1 so that null subsets are not counted
#                 result.append(sum(arr[i:j])) #inserting the sum into result array , we cannot use a predifined variable like maximum=0 because if all numbers are negetive then it will return 0 as it is greater than any negetive number
                
#         return max(result)
                
# #{ 
#  # Driver Code Starts
# #Initial Template for Python 3

# import math

 
# def main():
#         T=int(input())
#         while(T>0):
            
#             n=int(input())
            
#             arr=[int(x) for x in input().strip().split()]
            
#             ob=Solution()
            
#             print(ob.maxSubArraySum(arr,n))
            
#             T-=1


# if __name__ == "__main__":
#     main()



# OPTIMISED CODE


class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        max_sum = float('-inf')  # Initialize max_sum to negative infinity
    
        current_sum = 0
        for i in range(N):
            # add current iterating value to current sum
            current_sum += arr[i]
            # setting max sum as max value from current max sum and current sum
            max_sum = max(max_sum, current_sum)
            # checking if current sum is less than 0 , if it is then setting it to zero as adding more negetive numbers will lead to more reduce the  number further
            # or if we add positive number to negetive number the positive will be greater than the sum of both hence resseting the current_sum value
            if current_sum < 0:
                current_sum = 0
    
        return max_sum
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
