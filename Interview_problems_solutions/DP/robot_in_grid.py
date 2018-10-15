
def path_exists(grid,i,j):
	'''
	This algorithm finds whether there is a path between grid[i][j] and origin
	'''
	#print(i,j,A[i][j])
	if i < 0 or j < 0: # we are off the grid
		return False

	if i == j == 0: # reached origin

		return True if grid[i][j]==1 else False

	if A[i][j]==0: # obstacle, cannot go further back
		return False

	else: # recurse
		if path_exists(grid,i-1,j) or path_exists(grid,i,j-1):
			return True
		else:
			return False


def find_path(grid,i,j,path = [],memo = []):
	'''
	This algorithm finds whether there is a path between grid[i][j] and origin
	'''
	
	if i < 0 or j < 0: # we are off the grid
		return False
	if memo[i][j] != -1:
		return memo[i][j]

	#print(i,j)
	if i == j == 0: # reached origin
		#path.append((i,j)) # append start of the path
		if grid[i][j]==1:
			memo[i][j] = True
		else:
			memo[i][j] = False
		return memo[i][j]

	if A[i][j]==0: # obstacle, cannot go further back
		memo[i][j] = False
		return memo[i][j]

	else: # append path and recurse
		
		if find_path(grid,i-1,j,path=path,memo=memo) or find_path(grid,i,j-1,path=path,memo=memo):
			path.append((i,j)) # as we start emerging back from the bottom of the stack
			# we append the path in order of progression origin -> end
			return True, path
		else:
			return False

A =[
[1,1,0,0,1],
[1,1,0,1,1],
[0,1,1,1,0],
[0,1,0,1,1]
]

memo = [[-1 for j in A[0]] for i in A]

print(find_path(A,3,4,memo=memo))

