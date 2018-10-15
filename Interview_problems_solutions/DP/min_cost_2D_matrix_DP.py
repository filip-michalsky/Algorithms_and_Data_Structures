

import sys
import numpy as np

def minCostPath(cost,m,n):

	# cost is the matrix we are trying to traverse

	# m is the row idx of cost matrix
	# n is the column index of the cost matrix

	if (n < 0) or (m < 0):
		return sys.maxsize
	elif n == 0 and m == 0:
		return cost[m][n]
	else:
		return cost[m][n] + min (minCostPath(cost,m-1,n),\
			minCostPath(cost,m,n-1),minCostPath(cost,m-1,n-1)) 

cost = [[1, 2, 3],
		[4, 7, 20],
		[1, 4, 3]]

print(minCostPath(cost,2,2))