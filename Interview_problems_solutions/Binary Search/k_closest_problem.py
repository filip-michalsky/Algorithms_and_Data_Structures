# Given a sorted array, two integers k and x,
 # find the k closest elements to x in the array. 
 # The result should also be sorted in ascending order.
 #  If there is a tie, the smaller elements are always preferred.

# Example 1
#  Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]

# Example 2
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]

# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104

import bisect
import math
import time
class Solution:

	@staticmethod

	def findClosestElements(self, arr, k, x):
		"""
		:type arr: List[int]
		:type k: int
		:type x: int
		:rtype: List[int]
		"""
		result = arr[:k]  # store tentative result
		best_distance = sum([abs(i-x) for i in arr[:k]])
		#print(best_distance)

		for idx,j in enumerate(arr[:-k+1]): # need to leave k+1 spot in the end
			# print(arr[idx:idx+k])
			# print(idx+k)
			if best_distance-abs(arr[idx-1]-x)+abs(arr[idx+k-1]-x)<best_distance:
				best_distance = best_distance-abs(arr[idx-1]-x)+abs(arr[idx+k-1]-x)
				result =arr[idx:(k+idx)]
			          
		return result

	def findkClosest_faster(self, array, k, target):

		# if len(arr)==0:
		# 	return None

		# left = 0 # left pointer
		# right = len(arr)-k # right pointer
		# cnt =0
		# while right>left:
		# 	print(left)
		# 	print(right)
		# 	mid = (left+right)//2
		# 	#print(mid)
		# 	if abs(target - arr[mid]) < abs(arr[mid + k] - target):
		# 		right = mid
		# 		print('going right')
		# 	else:
		# 		right = mid
		# 		print('going left')
		# 	cnt+=1
		# return arr[left:left+k]
		left = right = bisect.bisect_left(array,target)
		print(left,right)
		while (right - left) < k:

			if left == 0: return array[:k]
			if right == len(array): return array[-k:]
			if target - array[left - 1] <= array[right] - target: left -= 1
			else: right +=1
		return array[left:right]
	
my_sol = Solution()

#print(my_sol.findClosestElements(my_sol,arr=[1,2,2,2,5,5,5,8,9,9],k=4,x=0))

#print(my_sol.findClosestElements(my_sol,arr=[1,1,2,3,3,3,4,6,8,8],k=6,x=1))

#print(my_sol.findClosestElements(my_sol,arr=[1],k=1,x=1))
start = time.time()
print(my_sol.findClosestElements(my_sol,arr=[0,1,2,2,2,3,6,8,8,9],k=2,x=8))
print(time.time()-start)
start = time.time()
print(my_sol.findkClosest_faster(array=[0,1,2,2,2,3,6,8,8,9],k=2,target=8))
print(time.time()-start)
