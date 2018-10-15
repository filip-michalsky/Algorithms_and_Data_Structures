class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 and nums[0]==0:
            return 1
        elif len(nums) == 1 and nums[0]==1:
            return 0
        
        dict_of_nums = {}
        min_num = 100000000
        max_num = -10000000

        for i in nums:
            dict_of_nums[i] = 1
            if i < min_num:
                min_num = i
            if i > max_num:
                max_num = i
        #print(min_num,max_num,dict_of_nums)
        for i in range(min_num,max_num+1):
            #print(i)
            try:
                if dict_of_nums[i] == 1:
                    continue
                else:
                    return i
            except:
                return i
        return max_num+1
A = [0,1]

sol = Solution()
print(sol.missingNumber(A))