
#!/usr/bin/env python

# The full permutation of list can be solved by picking any element, 
# placing it in the first, and recursively solving the smaller problem.

def perm(n, i):

    if i == len(n) - 1:
        print(n)
    else:
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            perm(n, i + 1)
            n[i], n[j] = n[j], n[i] # swap back, for the next loop
        
#perm([1, 2, 3], 0)



# Python function to print permutations of a given list 
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       candidates = permutation(remLst)
       print(candidates)
       for p in candidates: 
				 # this is for permutations WITHOUT DUPLICATES
              l.append([m] + p) 
    return l 

print(permutation([1,2,3]))
