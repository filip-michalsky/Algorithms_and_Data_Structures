import numpy as np

def isUnique(string): #exercise 1.1

	unique_dict = {} # define a hash table of unique vals

	for s in string:

		try:
			if unique_dict[s] == 1:
				#print(unique_dict[s])
				return False
		except KeyError:
			unique_dict[s] = 1

	return True

test_s = 'abcdefgha'

#print(isUnique(test_s))

def helper(string):
	'''Return a count table for unique chars'''
	count_dict = {}
	for s in string:
		try:
			count_dict[s]+=1
		except KeyError:
			count_dict[s] = 1
	return count_dict

def Check_Perm(S1, S2): # exercise 1.2

	if len(S1) != len(S2):
		return False

	count_dict1 = helper(S1)
	count_dict2 = helper(S2)

	for key, val in count_dict1.items():

		try:
			if val != count_dict2[key]:
				return False
		except KeyError:
			return False

	return True

S1 = 'aaaab'
S2 = 'aaaaa'

#print(Check_Perm(S1,S2))

def one_away_same_size(S1, S2):

	if len(S1) != len(S2): return False
	
	arr_mismatches = [True for i in S1] # True means mismatch here

	for idx, nums in enumerate(zip(S1, S2)):
		i, j = nums
		if i == j: # matching chars
			arr_mismatches[idx] = False

	if sum(arr_mismatches) <= 1: return True
	else: return False

def char_replaced_inserted(S1, S2):

	if abs(len(S1)-len(S2)) == 1: # one char away
		if len(S1) < len(S2):
			longer_arr = S2
			shorter_arr = S1
		else:
			longer_arr = S1
			shorter_arr = S2
	else:
		return False

	arr_mismatches = [True for i in longer_arr]

	mistakes_allowed = 0
	#print("longer: ", longer_arr, "shorter: ", shorter_arr)

	for idx, i in enumerate(longer_arr):
		#print(idx,i, mistakes_allowed, len(longer_arr))
		if idx == len(longer_arr)-1 and mistakes_allowed == 0:
			return True # edge case where we iterated through the entire array and no mistakes were found
			# this means the last char is inserted

		if mistakes_allowed == 1:
			idx -= 1 # if there is a mistake, shorter array is now trailing the longer one 
		
		if i == shorter_arr[idx]:
			arr_mismatches[idx] = False

		elif mistakes_allowed == 0 and i != shorter_arr[idx]:
			mistakes_allowed = 1
			# decrement idx

	if sum(arr_mismatches) == 1: return True
	else: return False

def one_Away(S1, S2): #exercise 1.5

	if abs(len(S1)-len(S2))>1:
		return False

	check_same_size = one_away_same_size(S1, S2)

	check_insert_replace = char_replaced_inserted(S1, S2)

	if check_same_size == True or check_insert_replace == True:

		return True
	else:
		return False

S1s = ['pale', 'pales', 'pale', 'pale', 'hrd', 'haadd']
S2s = ['ple', 'pale', 'bale', 'bake', 'hard','hkaadd']

for i, j in zip(S1s, S2s):
	print(one_Away(i,j))
































