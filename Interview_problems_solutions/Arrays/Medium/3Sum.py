class Solution(object):
    """
    Questions to ask before starting to solve the problem:
    What is the size of the list?
    What is the range of items? Negative numbers?
    Return one solution or all solutions?
    Can we use elements more than once?
    """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Complexity O(n^2)
        O(n) for each element and O(n) of scan of the consecutive elements.
        """
        nums.sort() # start by sorting the array
        #print(nums)
        N, result = len(nums), [] # N is the len of array
        for i in range(N): # iterate through the indices of the array
            if i > 0 and nums[i] == nums[i-1]: # to avoid duplicates in 3-SUM
            # once we have invoked 2-SUM from i+1, we will have received
            # all triples with i in it, including duplicates, thus we have to skip them
                continue
            target = nums[i]*-1 # once we determine a + b = -c, we reduce 3Sum to 2Sum
            start,end = i+1, N-1 # we use binary search to find the 2D sum

            while start < end: 
                #print(start,end)
                if nums[start]+nums[end] == target:
                    result.append([nums[i], nums[start], nums[end]])
                    start = start+1
                    # given nums[start], there is unique nums[end]
                    # S.T. nums[start] + nums[end] == target
                    # if nums[start+1] is the same as nums[start]
                    # then searching in range s+1 will give us a duplicate solution
                    # thus, we must move s till nums[s] != nums[s-1]
                    while start < end and nums[start] == nums[start-1]:
                        start = start+1 

                elif nums[start] + nums[end] < target:
                    start = start+1
                else:
                    end = end-1

        return result


nums = [-1, 0, 1, 2, -1, -4]
nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

# expected
#[[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]

sol = Solution()
print(sol.threeSum(nums))
        	


