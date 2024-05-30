# QUESTION
# Given two strings, s1 and s2, count the number of subsequences of string s1 equal to string s2.

# Return the total count modulo 1e9+7.

# Example 1:

# Input: s1 = geeksforgeeks, s2 = gks
# Output: 4
# Explaination: We can pick characters from s1 as a subsequence from indices {0,3,4}, {0,3,12}, {0,11,12} and {8,11,12}.So total 4 subsequences of s1 that are equal to s2.
# Example 2:

# Input: s1 = problemoftheday, s2 = geek
# Output: 0
# Explaination: No subsequence of string s1 is equal to string s2.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function countWays() which takes the string s1 and s2 as input parameters and returns the number of subsequences of s1 equal to s2.

# Expected Time Complexity: O(n*m)  [n and m are lengths of the strings s1 and s2]
# Expected Auxiliary Space: O(n*m)     [n and m are lengths of the strings s1 and s2]

# Constraints:
# 1 ≤ n, m ≤ 500  [n and m are lengths of the strings s1 and s2]


# NON OPTIMIZED SOLUTION
# import itertools
# class Solution:
#     def countWays(self, s1 : str, s2 : str) -> int:
#         result=0
#         for i in range(len(s1)+1):
#             for combinations in itertools.combinations(s1,i):
#                 if "".join(combinations)==s2:
#                     result+=1
#         return result
        


# #{ 
#  # Driver Code Starts
# if __name__ == "__main__":
#     t = int(input())
#     for _ in range(t):

#         s1 = (input())

#         s2 = (input())

#         obj = Solution()
#         res = obj.countWays(s1, s2)

#         print(res)





# OPTIMIZED SOLUTION
MOD = 10**9 + 7
m, n = len(s1), len(s2)

# dp[j] will store the number of ways to form s2[:j] using the current prefix of s1
dp = [0] * (n + 1)

# There's one way to form the empty subsequence
dp[0] = 1

for i in range(1, m + 1):
    # iterate backward to avoid overwriting values we still need to use
    for j in range(n, 0, -1):
        # If characters match, add the number of ways to form s2[:j-1] to s2[:j]
        if s1[i - 1] == s2[j - 1]:
            dp[j] = (dp[j] + dp[j - 1]) % MOD

return dp[n]
