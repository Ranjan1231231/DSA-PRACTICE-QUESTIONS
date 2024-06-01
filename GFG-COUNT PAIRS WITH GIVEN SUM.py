# QUESTION
# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


# Example 1:

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6.

# Example 2:

# Input:
# N = 4, K = 2
# arr[] = {1, 1, 1, 1}
# Output: 6
# Explanation: 
# Each 1 will produce sum 2 with any 1.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function getPairsCount() which takes arr[], n and k as input parameters and returns the number of pairs that have sum K.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


# UNOPTIMISED CODE O(N^2)
        # code here
        # i=2
        # result=0
        # for combinations in itertools.combinations(arr,i):
        #     if sum(combinations)==k:
        #         result+=1
        # return result


# OPTIMISED CODE O(N)

#User function Template for python3
import itertools
class Solution:
    def getPairsCount(self, arr, n, k):
        
        freq = {}
        count = 0
        
        for num in arr:
            complement = k - num
            if complement in freq:
                count += freq[complement]
            
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
