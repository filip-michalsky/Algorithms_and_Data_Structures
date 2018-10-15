from bisect import *

def climbingLeaderboard_sol1(scores, alice):
    result = []
    n= len(scores)
    m = len(alice)
    s = scores
    
    
    rnk = [0 for x in range(n)]
    ##Creating an array to contain rank values. The indices between this array and the score array will be the same for a particular score and its rank value.
    for i in range(0, n):
        if i==0:
            rnk[i+1] = 1
        else:
            rnk[i] = rnk[i-1];
            if s[i] < s[i-1]:
                rnk[i] = rnk[i] + 1;
    
    print(rnk)
    ##set a pointer for the bottom of the leaderboard
    p = n - 1
    ##for each of Alice's total scores after each level
    for i in range(0, m):
        x = alice[i]
        ans_smart = 0;
        
        ##comparing Alice's current total score and the leaderboard scores until Alice's score is 
        #less than or equal to a leaderboard score.
        while p > 0 and x > s[p]:
            p = p - 1
        
        ##use the pointer to set the current rank depending on whether Alice's score is equal or lesser.
        if x == s[p]:
            ans_smart = rnk[p];
        elif x < s[p]:
            ans_smart = rnk[p]+1;
        ##increment the rank because our array is zero-indexed.
        print(ans_smart + 1)
    return result

def climbingLeaderboard_sol2(scores, alice):
    
    scores = list(set(scores))
    l = len(scores)
    scores.sort()
    print(scores)
    for i in alice:
        print("alice score:",i)
        print("bisection:", bisect_right(scores, i))
        print (l - bisect_right(scores, i) + 1)

scores = [100, 100, 50, 40, 40, 20, 10]

alice = [5, 25, 50, 120]

print(climbingLeaderboard_sol2(scores,alice))