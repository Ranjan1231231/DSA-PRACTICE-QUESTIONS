# QUESTION
# Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

# Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 

# Example 1:

# Input:
# N = 4
# a[] = {0,3,1,2}
# Output: 
# -1
# Explanation: 
# There is no repeating element in the array. Therefore output is -1.
# Example 2:

# Input:
# N = 5
# a[] = {2,3,1,2,3}
# Output: 
# 2 3 
# Explanation: 
# 2 and 3 occur more than once in the given array.
# Your Task:
# Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in a sorted manner. 

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(n).


# UNOPTIMISED CODE
# class Solution:
#     def duplicates(self, arr, n): 
#         if arr==[]:
#             return [-1]
#             exit()
        
#         set_Arr=set(arr)
#         if len(arr)==len(set_Arr):
#             return [-1]
#             exit()
            
#         for i in set_Arr:
#             arr.remove(i)
        
#         arr2=sorted(set(arr))
#         return arr2
# #{ 
#  # Driver Code Starts
# if(__name__=='__main__'):
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int, input().strip().split()))
#         res = Solution().duplicates(arr, n)
#         for i in res:
#             print(i,end=" ")
#         print()


# SECOND UNOPTIMISED METHOD IS TO COUNTTHE OCCURENCE OF EACH ELEMENTS IN AN ARRAY , IF IT IS MORE THAN ONE THAN APPEND THAT ELEMENT IN A NEW ARRAY AND SORT IT AND USE SET OPERATION ON IT


# OPTIMISED CODE
    N = len(arr)
    duplicates = []

    for i in range(N):
        index = abs(arr[i])
        
        if arr[index] >= 0:
            arr[index] = -arr[index]
        else:
            duplicates.append(index)

    if not duplicates:
        return [-1]
    
    return sorted(duplicates)
