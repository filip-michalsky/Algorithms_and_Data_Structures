class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        This is a pretty fast solution!
        important: leverage hash tables as much as possible
        """
        total = 0
        len_s = len(s)
        i = 0
        mapping = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        while i< len_s-1:

        	if mapping[s[i]] < mapping[s[i+1]]:
        		total += mapping[s[i+1]] - mapping[s[i]]
        		i += 2
        	else:
        		total += mapping[s[i]]
        		i+= 1
        if i < len_s:
        	total += mapping[s[i]]
        	
        return total

    def exception_handler(self,char,next_char):

    	if char == 'I':
    		if next_char == "V":
    			return 4
    		elif next_char == "X":
    			return 9
    	elif char == "X":
    		if next_char == "L":
    			return 40
    		elif next_char == "C":
    			return 90
    	elif char == "C":
    		if next_char == "D":
    			return 400
    		elif next_char == "M":
    			return 900 
    	return False


test = "LVIII"

sol = Solution()

print(sol.romanToInt(test))
