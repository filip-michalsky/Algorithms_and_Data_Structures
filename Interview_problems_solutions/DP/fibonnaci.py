
def fib(n, memo = {}):
    '''
    Fibonnaci O(n), O(n) space

    '''
    if n in [0,1]: 
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
def fib_opti(n):

    a, b, i  = 0, 1, 2 # i starts at 2, bc we have fibonacci for 0 and 1
    while i < n:
        a, b = b, a +b
        i+=1
    return a+b

print(fib(30))
print(fib_opti(30))

