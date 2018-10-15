'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):

    if len(A) == 1 and A[0] != 1: return 1 # base case

    dict_of_nums = {}
    min_positive = 1000001
    max_positive = -1000001
    
    for i in A:
        dict_of_nums[i]=1
        if i < min_positive and i >0:
            min_positive = i
        if i > max_positive:
            max_positive = i
    
    if max_positive < 0:
        return 1
    #print(min_positive, max_positive)
    for i in range(1,max_positive+1): # need to start from 1!
        
        #if i not in dict_of_nums:
        #    return i
        try:
            if dict_of_nums[i] == 1:
                continue
            else:
                return i
        except:
            return i
    
    return max_positive+1


