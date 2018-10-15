class Solution():
	
	def convert(self, s, numRows):

		if numRows == 1 or numRows >= len(s):
			return s

		flag = 'ZIG' # direction : insert down
		Q = [i for i in s] # inititate the QUEUE
		i = 0 # initiate the pointer
		table_dict = {i:'' for i in range(numRows)} # initiate dict with results
		while Q:
			if flag == 'ZIG':
				while i <= numRows-1 and Q:
					table_dict[i] += Q.pop(0)
					i += 1
				flag = 'ZAG'
				i = numRows -1 
			else:
				while i-1 >= 0 and Q:
					table_dict[i-1] += Q.pop(0)
					i -= 1
				flag = 'ZIG'
				i = 1 # the first element in a new col is already inserted
		out = ''
		for i in range(numRows):
			out+=table_dict[i]
		return out



sol = Solution()
s = "PAYPALISHIRING"
numRows = 4

print(sol.convert(s = s, numRows = numRows))

print(2**31)