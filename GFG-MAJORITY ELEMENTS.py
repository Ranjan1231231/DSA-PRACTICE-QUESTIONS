# QUESTION
# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.
 

# Example 1:

# Input:
# N = 3 
# A[] = {1,2,3} 
# Output:
# -1
# Explanation:
# Since, each element in 
# {1,2,3} appears only once so there 
# is no majority element.
# Example 2:

# Input:
# N = 5 
# A[] = {3,1,3,3,2} 
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is 
# the majority element.

# UNOPTIMIZED CODE O(N^2)

#User function template for Python 3

# class Solution:
#     def majorityElement(self, A, N):
#         #Your code here
#         # for i in A:
#         #     if A.count(i)>(N/2):
#         #         return i
#         # return -1
        


# #{ 
#  # Driver Code Starts
# #Initial Template for Python 3

# import math

# from sys import stdin


# def main():
#         T=int(input())
#         while(T>0):
            
#             N=int(input())

#             A=[int(x) for x in input().strip().split()]
            
            
#             obj = Solution()
#             print(obj.majorityElement(A,N))
            
#             T-=1


# if __name__ == "__main__":
#     main()
# # } Driver Code Ends


# OPTIMIZED CODE O(N)
curr_num=None
count=0
for i in A:
    if count==0:
        curr_num=i
    if curr_num==i:
        count+=1
    else:
        count-=1

if A.count(curr_num)>N/2:
    return curr_num
else:
    return -1
