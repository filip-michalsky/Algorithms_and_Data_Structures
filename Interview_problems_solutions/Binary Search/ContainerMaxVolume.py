class Solution:

    def maxArea(self,height):
        # binary search!!
        left, right, result = 0, len(height)-1, 0

        while left<right:
            area = (right - left) * min(height[left],height[right])
            result = max (result,area)
            if height[right] < height[left]: right -= 1 # if the left boundary is higher, decrement right boundary index
            else: left +=1 # if right boundary is higher than left boundary, decrement it
        return result
        
        def maxArea_brute(self, height):
        """
        :type height: List[int]
        :rtype: int

        ##################
        # this is brute force, too slow!!
        ##################

        """
        # base case
        if len(height) == 2:
            return min(height)
        
        max_vol = 0
        for idx1, val1 in enumerate(height):
            for idx2, val2 in enumerate(height[idx1:]):
                volume = (idx2)*min(val1,val2)
                if volume > max_vol:
                    max_vol = volume
        return max_vol

a = [1,8,6,2,5,4,8,3,7]

sol = Solution()

print(sol.maxArea(a))