class Solution:
    def letterCombinations_slow(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        THIS IS SLOW BUT PASSING!!!
        """
        digit_list = [i for i in digits]
        if len(digit_list)==0:
            return []
        start = digit_list.pop(0)
        m, n = 0, 0 
        mapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        for i in digit_list:
            if int(i) in [7,9]:
                m += 1
            else:
                n += 1
        start_length = (4**m)*(3**n)
        
        start_arr = []
        counter = 0 
        for i in range(start_length):
            Q = mapping[start].copy()
            while Q:
                a = Q.pop(0)
                start_arr.append(a)
                counter+=1

        start_arr = sorted(start_arr)
        remain_len = len(start_arr)
        while digit_list:
            counter = 0
            digit = digit_list.pop(0)
            start_arr = sorted(start_arr)
            while counter < remain_len:
                Q = mapping[digit].copy()
                while Q:
                    a = Q.pop(0)
                    start_arr[counter]+=a
                    counter+=1
        return start_arr

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(digits == ""):
            return []
        nums = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = [""]
                    
        
        for d in digits: # loop through the digits
            
            temp = []
            for c in nums[int(d)]: # loop through the possible values for the number input
                for k in result: # 
                    print(c,k)
                    temp.append(k+c)
                
            result = temp

                
                

        return result
        
        
sol = Solution()
ans = sol.letterCombinations("247")
print(ans)
print(len(set(ans)),len(ans))