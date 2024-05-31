# # QUESTION
# Given a number n, Your task is to swap the two nibbles and find the resulting number. 

# A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte. For example, the decimal number 150 is represented as 10010110 in an 8-bit byte. This byte can be divided into two nibbles: 1001 and 0110.

# Example 1:

# Input: n = 100
# Output: 70
# Explanation: 100 in binary is 01100100, two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.
# Example 2:

# Input: n = 129
# Output: 24
# Explanation: 129 in binary is 10000001, two nibbles are (1000) and (0001). If we swap the two nibbles, we get 00011000 which is 24 in decimal.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function swapNibbles() which takes an integer n as input parameter and returns an integer after swapping nibbles in the binary representation of n.

# Expected Time Complexity: O(1)
# Expected Space Complexity: O(1)

# Constraints:
# 0 ≤ n ≤ 255


# UNOPTIMIZED CODE O(N LOG N)

# #User function Template for python3
# class Solution:
#     def swapNibbles (self, n):
#         # k=bin(n)
#         # tempstring=""
#         # if len(k[2:])==8:
#         #     tempstring+=k[2:]
#         # else:
#         #     tempstring=(8-len(k[2:]))*"0"
#         #     tempstring+=k[2:]
#         # newnum=tempstring[4:8]+tempstring[0:4]
#         # return(int(newnum,2))


# #{ 
#  # Driver Code Starts
# #Initial Template for Python 3
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())

#         ob = Solution()
#         print(ob.swapNibbles(n))

# # } Driver Code Ends

# # OPTIMIZED CODE O(1)
    n &= 0xFF
    
    # Extract the lower 4 bits and the upper 4 bits
    lower_4_bits = n & 0x0F
    upper_4_bits = (n >> 4) & 0x0F
    
    # Swap the lower and upper 4 bits
    new_num = (lower_4_bits << 4) | upper_4_bits
    
    return new_num



