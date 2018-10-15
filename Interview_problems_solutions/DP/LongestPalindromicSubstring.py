class Solution:


    def longestPalindrome_brute(self, s):

        """
        :type s: str
        :rtype: str

        the brute force solution requires O(n^3) time and O(n) space
        """
        repeats = {}
        if len(s) == 0:
            return ""
        
        elif len(s) == 1:
            return s
        longest_palidrome = ''
        
        for idx,i in enumerate(s):
            
            current_expression = i
            
            if current_expression not in repeats:
                if self.check_palidrome(current_expression):
                    if len(current_expression) > len(longest_palidrome):
                        longest_palidrome = current_expression

            repeats[current_expression] = 1
            for j in s[idx+1:]:
                current_expression +=j
                if current_expression not in repeats:
                    if self.check_palidrome(current_expression):
                        if len(current_expression) > len(longest_palidrome):
                            longest_palidrome = current_expression

                repeats[current_expression] = 1
        return longest_palidrome



    def check_palidrome(self,s):
        if type(s) != str:
            raise TypeError
        return s == s[::-1]



    def longestPalindrome_Man(self,s):
        # O(n) Manacher’s algorithm
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in range(1,len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]

    def longestPalindrome_DP(self,s):
        '''
        We could see that the longest common substring method fails 
        when there exists a reversed copy of a non-palindromic substring in 
        some other part of SS. To rectify this, each time we find a longest 
        common substring candidate, we check if the substring’s indices are the 
        same as the reversed substring’s original indices. If it is, then we attempt 
        to update the longest palindrome found so far; if not, we skip this and find the next candidate.

        This gives us an O(n^2) Dynamic Programming solution which uses O(n^2)
        space (could be improved to use O(n) space).
        '''

        if len(s) in [0,1]:
            return s

        memo = [True for _ in range(2*len(s))] #initiate the memo table

        maxLen = 1
        start = 0

        for length in range(1,len(s)+1):
            for i in range(len(s)-length+1): # iterate through substring starting indices

                j = i + length - 1
                #print(i,j)
                if memo[i+j]:
                    if s[i]==s[j]:
                        start = i

                        maxLen = max(maxLen,length)
                    else:
                        memo[i+j] = False
        return s[start:start+maxLen]

        



test = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"

sol = Solution()
test2 = 'bb'


#print(sol.longestPalindrome_brute(test))

print(sol.longestPalindrome_DP(test))












