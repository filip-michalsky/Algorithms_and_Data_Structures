from time import time

class Solution1: # correct solution, but slow
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_digits = set() # set of digits in the current window

        past_digits = {} # track past digits
        past_digits_idx = {} # track past digit indices
        longest_substring = 0
        curr_length = 0

        for idx, char in enumerate(s):

            if char not in current_digits:
                current_digits.add(char)
                curr_length += 1
                past_digits[char] = idx
                past_digits_idx[idx]= char
                if curr_length >= longest_substring:
                    longest_substring = curr_length
            else:
                last_idx = past_digits[char]
                curr_length = idx-last_idx
                past_digits[char] = idx
                past_digits_idx[idx] = char
                current_digits = set([past_digits_idx[i] for i in range(last_idx,idx)]) # this is probably inefficient
                
        return longest_substring


class Solution2: # wrong solution! - read-up on faster implementation
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        past_digits = {} # track past digits
        curr_elems = set()
        curr_window = [0,0]
        max_len = 0 

        for idx, char in enumerate(s):

            if char not in curr_elems: # if element not in set, add it and increment window
                curr_elems.add(char)
                curr_window[1] = idx
                past_digits[char] = idx
                window_size = curr_window[1]-curr_window[0]

                if window_size >=max_len:
                    max_len = window_size
            
            else:
                past_idx = past_digits[char] # retrieve past index of the current repeating char

                if past_idx>=curr_window[0]: # only update the idx of start of the window if higher than current window start
                    curr_window = [past_idx,idx]

                if window_size >=max_len:
                    max_len = window_size
                past_digits[char] = idx # assign new idx to the char (so that it does not repeat)
            
        return max_len


input_s = "aabcaaasyqwertyuioafsasf"
#input_s = "aabc"
#input_s = "pwwkew"
#input_s = 'bfyfygybg'

solution = Solution1()

print('Input string: ',input_s)

start = time()
print('Solution 1:\n',solution.lengthOfLongestSubstring(input_s),'\n','-'*50)
sol1_t = time()-start

solution2 = Solution2()

start = time()
print('Solution 2:\n',solution2.lengthOfLongestSubstring(input_s),'\n','-'*50)
sol2_t = time()-start

if sol1_t<sol2_t:
    print('Solution 1 is faster')
    print(sol2_t-sol1_t)
else:
    print('Solution 2 is faster')
    print('{}'.format(sol1_t-sol2_t))
