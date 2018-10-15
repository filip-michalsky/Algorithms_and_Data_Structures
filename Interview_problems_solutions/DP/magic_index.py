
def magic_index_brute(A,i=0):

    if A[i] == i: # found what we need!
    	return i
    else:
    	if i < len(A)-1:
    		return magic_index(A,i+1) # recurse on right part of substring
    	else: # base cases, end of string reached
    		return False

def magic_index(A,start,end):
	#print(start,end)
	# binary search implemented using DP

	if end < start:
		return -1
	mid = (start + end) //2
	if A[mid] == mid:
		return mid
	elif A[mid] < mid:
		return magic_index(A,mid+1,end)
	else:
		return magic_index(A,start,mid-1)

def magic_index_repeats(A,start,end):
	#print(start,end)
	# binary search implemented using DP

	if end < start:
		return -1

	midIndex = (start + end) // 2
	midValue = A[midIndex]
	if midIndex == midValue: # if we allow repeats we have to search both right and left
		return midIndex

	left_idx = min(midIndex-1,midValue)
	left = magic_index(A,start,left_idx)
	
	if left >=0:
		return left

	right_idx = max(midIndex+1,midValue)
	right = magic_index(A,right_idx,end)

	return right




A =[-1,-1,-1, -1, -1, -1, -1, -1]

print(magic_index_repeats(A,start=0,end=len(A)-1))