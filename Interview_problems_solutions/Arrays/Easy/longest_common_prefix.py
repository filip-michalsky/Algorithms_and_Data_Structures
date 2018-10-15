class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        max_len = 1000000
        shortest_str_idx = 0
        for idx in range(len(strs)):
        	if len(strs[idx])<max_len:
        		max_len = len(strs[idx])
        		shortest_str_idx = idx
        comparison = strs.pop(shortest_str_idx)
        Q = [i for i in comparison]
        pointer = 0
        match = ""
        END = False
        while Q:
        	item = Q.pop(0)
        	for i in strs:
        		if item != i[pointer]:
        			END = True
        			break
        	if not END:
        		match += item
        		pointer += 1
        	else:
        		break
        return match

test = ['ccb','ccb','ccb']
sol = Solution()
print(sol.longestCommonPrefix(test))