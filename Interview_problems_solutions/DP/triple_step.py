
def triple_step(n, memo = {}):

    # base cases
    if n in [0,1,2]: # if there are 0 1 or 
        return n
    elif n == 3:
        return 4
    else:
        memo[n] = triple_step(n-1) + triple_step(n-2) + triple_step(n-3) # the child can only hop 1, 2 or 3 steps in the last iteration
        return memo[n] 

print(triple_step(10))