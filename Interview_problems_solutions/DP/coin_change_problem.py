
'''
Coing-change problem.

Similar to Knap-sack.

1) Optimal Substructure
To count the total number of solutions, we can divide all set solutions into two sets.
1) Solutions that do not contain mth coin (or Sm).
2) Solutions that contain at least one Sm.
Let count(S[], m, n) be the function to count the number of solutions, then it can be written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).

Therefore, the problem has optimal substructure property as the problem can be solved using solutions to subproblems.

2) Overlapping Subproblems
Following is a simple recursive implementation of the Coin Change problem. The implementation simply follows the recursive structure mentioned above.
 
'''

# Recursive Python3 program for 
# coin change problem. 
  

# Returns the count of ways we can sum 
# S[0...m-1] coins to get sum n 
def count(S, m, n ): 
  
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1
  
    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0; 
  
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and n >= 1): 
        return 0
  
    # count is sum of solutions 
    # (i) including S[m-1]
    # (ii) excluding S[m-1] 

    return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 

# Driver program to test above function 
arr = [1, 2, 3, 4] 
m = len(arr) 
print(count(arr, m, 4)) 


# Dynamic Programming Python implementation of Coin  
# Change problem 

def count_dp(S, m, n): 
    # We need n+1 rows as the table is constructed  
    # in bottom up manner using the base case 0 value 
    # case (n = 0) 
    # m ... m coins available
    # n ... sum we need
    table = [[0 for x in range(m)] for x in range(n+1)] 
    print(table)
    # if we have no coins, there is only one solution -> no change!
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
  
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): # 
        for j in range(m): 
  
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
  
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
  
            # total count 
            table[i][j] = x + y 
    
    print(table)
    return table[n][m-1] 
  
# Driver program to test above function 
arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(count_dp(arr, m, n)) 