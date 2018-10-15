
### Problem Solved Using: simple while loops


class Solution:
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		verbose = False
		spiral = matrix
		total_cnt = 0
		visited = {} # visited nodes
		for row_idx,row in enumerate(spiral):
			for col_idx,val in enumerate(row):
				visited[row_idx,col_idx] = 0
				total_cnt+=1

		direc = 'right'
		pointer_row, pointer_col = 0,0
		cnt = 0
		result = []

		while cnt < total_cnt:

			if direc == "right":

				while pointer_col < len(spiral[0]) and visited[pointer_row,pointer_col] ==0:
					if verbose:
						print(spiral[pointer_row][pointer_col])
					result.append(spiral[pointer_row][pointer_col])
					visited[pointer_row,pointer_col] = 1
					pointer_col +=1 
					cnt+=1
				direc = 'down'
				pointer_col-=1 # to account for the last non-existing val
			
			if direc == 'down':
				if pointer_row <= len(spiral):
					pointer_row+=1
				
				while pointer_row < len(spiral) and visited[pointer_row,pointer_col] ==0:
					if verbose:
						print(spiral[pointer_row][pointer_col])
					result.append(spiral[pointer_row][pointer_col])
					visited[pointer_row,pointer_col] = 1
					pointer_row += 1
					cnt+=1
				direc = 'left'
				pointer_row-=1

			if direc == 'left':
				if pointer_col <= len(spiral[0]):
					pointer_col-=1
				
				while pointer_col >= 0 and visited[pointer_row,pointer_col] ==0:
					if verbose:
						print(spiral[pointer_row][pointer_col])
					result.append(spiral[pointer_row][pointer_col])
					visited[pointer_row,pointer_col] = 1
					pointer_col -=1 
					cnt+=1
				direc = 'up'
				pointer_col+=1

			if direc == 'up':
				
				pointer_row-=1
				
				while pointer_row >= 0 and visited[pointer_row,pointer_col] ==0:
					if verbose:
						print(spiral[pointer_row][pointer_col])
					result.append(spiral[pointer_row][pointer_col])
					visited[pointer_row,pointer_col] = 1
					pointer_row -= 1
					cnt+=1
				
				direc = 'right'
				pointer_row += 1
				pointer_col += 1
		return result

spiral = [
[1,2,3,4,77],
[4,5,6,14,87],
[7,8,9,24,99],
[70,80,95,40,90]
]

sol = Solution()
print('-'*40)
print(sol.spiralOrder(spiral))
print('-'*40)

