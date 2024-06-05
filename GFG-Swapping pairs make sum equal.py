# QUESTION

# Given two arrays of integers a[] and b[] of size n and m, the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.

# Note: Return 1 if there exists any such pair otherwise return -1.

# Example 1:

# Input: n = 6, m = 4, a[] = {4, 1, 2, 1, 1, 2}, b[] = (3, 6, 3, 3)
# Output: 1
# Explanation: Sum of elements in a[] = 11, Sum of elements in b[] = 15, To get same sum from both arrays, we can swap following values: 1 from a[] and 3 from b[]
# Example 2:

# Input: n = 4, m = 4, a[] = {5, 7, 4, 6}, b[] = {1, 2, 3, 8}
# Output: 1
# Explanation: We can swap 6 from array a[] and 2 from array b[]
# Expected Time Complexity: O(mlogm+nlogn).
# Expected Auxiliary Space: O(1).



# UNOPTIMIZED CODE 1 O(N^2*M +N*M^2)
# for i in range(n):
        #     for k in range(m):
        #         temparr1=a.copy()
        #         temparr1.pop(i)
        #         temparr1.append(b[k])
        #         temparr2=b.copy()
        #         temparr2.pop(k)
        #         temparr2.append(a[i])
        #         if sum(temparr1)==sum(temparr2):
        #             return 1
        # return -1

# UNOPTIMIZED CODE 2 O(M+N)
# # LOGIC-
        # # suma-a[i]+b[j]==sumb-b[j]+a[i]
        # # 2b[j]=sumb-suma+2a[i]
        
        # barray_elements=[]
        # for i in b:
        #     barray_elements.append(2*i)
        ## converting to set as it has less time complexity to look for an elemnt through it
        # setb=set(barray_elements)
        # suma=sum(a)
        # sumb=sum(b)
        # for i in range(n):
        #     if ((sumb-suma)+(2*(a[i]))) in setb:
        #         return 1
        # return -1


# OPTIMIZED CODE O(N+M)
        # Calculate sums of both arrays
        sumA = sum(a)
        sumB = sum(b)
        # Calculate the difference
        diff = sumB - sumA
        # If diff is odd, we cannot split it evenly
        if diff % 2 != 0:
            return -1
        # Calculate the target difference
        target = diff // 2
        # Store elements of b in a set for quick lookup
        setB = set(b)
        # Check for each element in a if there exists a corresponding element in b
        for x in a:
            if (x + target) in setB:
                return 1
        # If no such pair is found, return -1
        return -1

