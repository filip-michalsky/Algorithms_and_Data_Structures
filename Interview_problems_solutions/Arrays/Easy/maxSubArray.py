
### Problem Solved Using:
### Given an integer array nums, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
 
import math

class Solution():
	def maxSubArray(self,nums):
	# Maintain a running_total of the array seen so far.
	# If the current value is greater than the current running total, set the running total to the current value.
	# Track the maximum total seen so far and return it.
		running_total = maximum = nums[0]

		for i in nums[1:]:

			running_total = max(running_total+i,i)
			maximum = max(running_total,maximum)

		return maximum
sol = Solution()

arr2 = [5,-11,3,4]
arr3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(arr3))
