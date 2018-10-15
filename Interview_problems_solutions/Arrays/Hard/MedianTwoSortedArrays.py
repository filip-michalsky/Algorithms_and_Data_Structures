
### Problem Solved Using:

### Divide and Conquer Algorithm (Binary Search)

import math
import numpy as np

class Solution2():
	def median(self,A, B):
	    m, n = len(A), len(B)
	    if m > n:
	        #print('A longer than B')
	        A, B, m, n = B, A, n, m
	    #print(len(A),len(B),m,n)
	    if n == 0:
	        raise ValueError

	    imin, imax, half_len = 0, m, (m + n + 1) / 2
	    while imin <= imax:
	        i = int((imin + imax) / 2)
	        j = int(half_len - i)

	        if i < m and B[j-1] > A[i]:
	            # i is too small, must increase it
	            imin = i + 1
	        elif i > 0 and A[i-1] > B[j]:
	            # i is too big, must decrease it
	            imax = i - 1
	        else:
	            # i is perfect
	            if i == 0: max_of_left = B[j-1]
	            elif j == 0: max_of_left = A[i-1]
	            else: max_of_left = max(A[i-1], B[j-1])

	            if (m + n) % 2 == 1:
	                return max_of_left

	            if i == m: min_of_right = B[j]
	            elif j == n: min_of_right = A[i]
	            else: min_of_right = min(A[i], B[j])

	            return (max_of_left + min_of_right) / 2.0



arr1 = [1,2,5,9,10]
arr2 = [12,13,14,18]

print('Length of arrays: ',len(arr1+arr2))
merge_arr =sorted(arr1+arr2)
print(merge_arr)
print('True: ', int(np.median(np.array(merge_arr))))


sol2 = Solution2()

print('Leetcode solution: ',sol2.median(arr1,arr2))


