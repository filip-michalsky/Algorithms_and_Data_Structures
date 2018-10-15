
import math
class Solution():
	def twoSum(self,nums,target):
        
        # create a dictionary to store value: target - val 
        # anytime we get to a new element, if values is in the 
        # dictionary, then we know target - val = curr_val 
        # hence we found a pair which sums to the target and 
        # we can return the indices.
		dict_items = {}
		list_of_idx = []
        
		for idx, val in enumerate(nums):
            
			
			if val in dict_items:
				list_of_idx.append(dict_items[val])
				list_of_idx.append(idx)
				return list_of_idx
			dict_items[target - val]= idx

sol = Solution()

arr = [3,2,4]
target = 6

print(sol.twoSum(arr,target))
