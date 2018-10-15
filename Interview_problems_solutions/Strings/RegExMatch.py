class Solution():


    # def isMatch1(self, s, p, s_index=0, p_index=0, cache=None):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool

    #     This is a DP problem -> return to it!!
    #     """
    #     if not cache:
    #         cache = [[ None for _ in range(len(p))] for _ in range(len(s))]
            
    #     if s_index < len(s) and p_index < len(p) and cache[s_index][p_index] is not None:
    #         return cache[s_index][p_index]

    #     if p_index >= len(p):
    #         return s_index >= len(s)
    #     if p_index + 1 < len(p) and p[p_index + 1] == '*':
    #         is_matched = self.isMatch(s, p, s_index, p_index + 2, cache) or \
    #                 ((s_index < len(s) and (p[p_index] == '.' or s[s_index] == p[p_index])) and \
    #                  self.isMatch(s, p, s_index + 1, p_index, cache))
    #     else:
    #         is_matched = (
    #             s_index < len(s) and (p[p_index] == '.' or s[s_index] == p[p_index]) and \
    #             self.isMatch(s, p, s_index + 1, p_index + 1, cache)
    #         )
        
    #     if s_index < len(s) and p_index < len(p):
    #         cache[s_index][p_index] = is_matched

    #     return is_matched

    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def isMatchTopDown(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text) # Am I in the end?
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    def isMatchBottomUP(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


sol = Solution()

string = "mississippi"
pat = "mis*is*ip*."



print(sol.isMatchBottomUP(string,pat))# 'E:',True,string,pat)


s1 = "aa"
p1 = "a"
s2 = "aa"
p2 = "a*"
s3 = "ab"
p3 = ".*"
s4 = "aab"
p4 = "c*a*b" # FIX THIS!

s5 = "mississippi"
p5 = "mis*is*p*."
s6 = "ab"
p6 = ".*c"
s7 = "aaa"
p7 = "aaaa"
s8 = "aaa"
p8 = "a.a"

s9 = "aaa"
p9 = "ab*a"

ins = [(s1,p1),(s2,p2),(s3,p3),(s4,p4),(s5,p5),(s6,p6),(s7,p7),(s8,p8),(s9,p9)]
outs = [False,True,True,True,False,False,False,True,False]

for idx,sp in enumerate(ins):
	s,p = sp
	#print('\n')
	print(sol.isMatchBottomUP(s,p)==outs[idx])#,s,p)



	# # passing 355/447 test cases
	# def isMatch(self, s, Q_p):
	# 	if len(s) == 0 or len(Q_p) == 0:
	# 		return False
	# 	Q_s = [ i for i in s]
	# 	j, len_s, len_p = 0, len(s), len(Q_p)
	# 	MULTI_POP = False
	# 	used_pattern = {j:0 for j in range(len_p)}
	# 	while Q_s:

	# 		if not MULTI_POP:
	# 			char = Q_s.pop(0)
	# 		#print(char,j)
	# 		MULTI_POP = False
	# 		#print("\n",char)
	# 		if j+1 <= len_p-1:
	# 			# print('j:',j)
	# 			# print('current char',char)
	# 			# print('pattern position',Q_p[j])
	# 			if Q_p[j+1] == '*':
	# 				#print('we got a star on next position')
	# 				if Q_p[j] == '.' : #'.*' will be always true
	# 				 	# now, need to check whether there is an additional char after .* pattern
	# 				 	if j+2 <= len_p -1: # we are not at the end of the pattern
	# 				 		while True:
	# 				 			if char != Q_p[j+2] and Q_s:
	# 				 				#print('we found .*',char,j)
	# 			 					used_pattern[j] = 1
	# 			 					used_pattern[j+1]=1
	# 				 				char = Q_s.pop(0)
	# 				 				MULTI_POP = True
	# 				 			else:
	# 				 				break
	# 				 		#print('ended while, now at char',char,Q_s,j)
	# 				 		if not Q_s and j+2 <= len_p -1: 
	# 				 			#print(used_pattern)
	# 				 			return False
	# 				 	else: # at the end of the pattern, can cover everything
	# 				 		used_pattern[j+1]=1
	# 				 		#print(used_pattern)
	# 				 		return True


	# 				while char == Q_p[j] and Q_s: # keep removing chars if they match pattern char before star
	# 					#print('removing',char)
	# 					char = Q_s.pop(0)
	# 					MULTI_POP = True
	# 					used_pattern[j] = 1
	# 					used_pattern[j+1] = 1

	# 				if j + 2 <= len_p -1: # there is a char after *
	# 					#print('there is a char after *')
	# 					if Q_p[j] == Q_p[j+2] or '.' in [Q_p[j],Q_p[j+2]]: # the char before after star are the same
	# 						#print('same char before after')
	# 						if j+3 <= len_p -1:

	# 			 				used_pattern[j] = 1
	# 			 				used_pattern[j+1] = 1
	# 			 				used_pattern[j+2] = 1
	# 			 				j = j+3

	# 						else: # we are at the end of the pattern string we either looped 
	# 						#hrough the whole original string or the pattern does not match
	# 							if Q_s:
	# 								#print(used_pattern)
	# 								return False
									
	# 							else:
	# 								#print(used_pattern)
	# 								return True
	# 					else:
	# 						#print('there is a char after, but the one before is not matching')
	# 						used_pattern[j] = 1
	# 						used_pattern[j+1] = 1
	# 						j = j+2
	# 						used_pattern[j] = 1
	# 						continue

	# 		if j <= len_p-1 and (char == Q_p[j] or Q_p[j] == '.'):
	# 			#print('match:',char,Q_p[j])
	# 			used_pattern[j] = 1
	# 			j+=1
	# 			#used_pattern[j] = 1
			
	# 		# elif not Q_s and (char == Q_p[j] or char == '.'):#end of string is .
	# 		# 	if j <= len_p-1:
	# 		# 		j+=1
	# 		else:
	# 			#print('not true') ## need to adjust this! Why is this example not working?
	# 			#print(used_pattern)
	# 			return False
	# 	# if j>= len_p-1:
	# 	# 	return False
	# 	print('ended while:',used_pattern)
	# 	for i in used_pattern:
	# 		if used_pattern[i]==0:
	# 			return False
	# 	return True
