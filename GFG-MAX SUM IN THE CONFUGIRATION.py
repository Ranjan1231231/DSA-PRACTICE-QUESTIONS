# QUESTION
# Given an integer array(0-based indexing) a of size n. Your task is to return the maximum value of the sum of i*a[i] for all 0<= i <=n-1, where a[i] is the element at index i in the array. The only operation allowed is to rotate(clockwise or counterclockwise) the array any number of times.

# Example 1:

# Input: n = 4, a[] = {8, 3, 1, 2}
# Output: 29
# Explanation: All the configurations possible by rotating the elements are:
# 3 1 2 8 here sum is 3*0+1*1+2*2+8*3 = 29
# 1 2 8 3 here sum is 1*0+2*1+8*2+3*3 = 27
# 2 8 3 1 here sum is 2*0+8*1+3*2+1*3 = 17
# 8 3 1 2 here sum is 8*0+3*1+1*2+2*3 = 11, so the maximum sum will be 29.
# Example 2:

# Input: n = 3, a[] = {1, 2, 3}
# Output: 8
# Explanation: All the configurations possible by rotating the elements are:
# 1 2 3 here sum is 1*0+2*1+3*2 = 8
# 3 1 2 here sum is 3*0+1*1+2*2 = 5
# 2 3 1 here sum is 2*0+3*1+1*2 = 5, so the maximum sum will be 8.
# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).


# UNOPTIMIZED O(N^2)
    # maximum=0
    # for i in range(n):
    #     total=0
    #     for j in range(n):
    #         total+=a[j]*j
    #     if maximum<total:
    #         maximum=total
    #     a.append(a[0])
    #     a.pop(0)
    # return maximum

# OPTIMIZED O(N)
#User function Template for python3

def max_sum(a,n):
    #code here
    
    # Calculate the initial sum S_0
    S_0 = sum(i * a[i] for i in range(n))
    max_sum = S_0
    
    # Calculate the sum of the array
    array_sum = sum(a)
    
    # Iteratively calculate sums for rotations
    S = S_0
    for i in range(1, n):
        S = S + array_sum - n * a[n-i]
        max_sum = max(max_sum, S)
    
    return max_sum
    
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends
