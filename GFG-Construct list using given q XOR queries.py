# QUESTION
# Given a list s that initially contains only a single value 0. There will be q queries of the following types:

# 0 x: Insert x in the list
# 1 x: For every element a in s, replace it with a ^ x. ('^' denotes the bitwise XOR operator)
# Return the sorted list after performing the given q queries.

# Example 1:

# Input:
# q = 5
# queries[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
# Output:
# 1 2 3 7
# Explanation:
# [0] (initial value)
# [0 6] (add 6 to list)
# [0 6 3] (add 3 to list)
# [0 6 3 2] (add 2 to list)
# [4 2 7 6] (XOR each element by 4)
# [1 7 2 3] (XOR each element by 5)
# The sorted list after performing all the queries is [1 2 3 7]. 
# Example 2:
# Input:
# q = 3
# queries[] = {{0, 2}, {1, 3}, {0, 5}} 
# Output :
# 1 3 5
# Explanation:
# [0] (initial value)
# [0 2] (add 2 to list)
# [3 1] (XOR each element by 3)
# [3 1 5] (add 5 to list)
# The sorted list after performing all the queries is [1 3 5].

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function constructList() which takes an integer q the number of queries and queries[] a list of lists of length 2 denoting the queries as input parameters and returns the final constructed list.


# Expected Time Complexity: O(q*log(q))
# Expected Auxiliary Space: O(l), where l is only used for output-specific requirements.


# UNOPTIMIZED CODE O(N^2)
        # code here
        # arr=[0]
        # for i in queries:
        #     arraylen=len(arr)
        #     if i[0]==0:
        #         arr.append(i[1])
        #     elif i[0]==1:
        #         for index in range(arraylen):
        #             arr[index]=arr[index]^i[1]
        # arr.sort()
        # return arr


# OPTIMIZED CODE O(N LOG N)


from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
                  
        # setting up the array  
        arr = [0]
        
        xor_val = 0
        
        for i in queries:
            if i[0] == 0:
                # the below line ensures the element is adjusted for any previous xor operations
                arr.append(i[1]^xor_val)
            elif i[0] == 1:
                xor_val ^= i[1]
        
        arr = [x ^ xor_val for x in arr]
        arr.sort()
        return arr



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


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
    t = int(input())
    for _ in range(t):

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.constructList(q, queries)

        IntArray().Print(res)
