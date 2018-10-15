class Solution():
    '''
    DFS operating on an ADJACENCY MATRIX

    This algorithm is the same as a landfill:
    Counting the number of connected components.

    '''
    def dfs(self, M, i): # i refers to the ith row in the adjacency matrix

        for j in range(len(M[0])): #iterate through friends list of I
            if M[i][j] == 1 and self.visited[j] == 0: # if J is a friend of I 
            # and we have not visited J yet
                self.visited[j] = 1
                if all(self.visited)==1: #if I know that all nodes have been visited, I can end the recursion
                    return
                self.dfs(M,j)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0: # base case: no friends no circles
            return 0

        # initiate the count of connected components
        count = 0
        # array keeping track of visited persons( 1-visited, 0-not visited)
        self.visited = [0]*len(M) # I could make it even faster by changing this to a dict

        for i in range(len(M)):
            if self.visited[i] == 0: # this person has not been visited yet
                self.visited[i] = 1 # mark as visited
                self.dfs(M,i)
                count+=1
        return count
        



if __name__ == '__main__':

    M1 = [[1,1,0],[1,1,1],[0,1,1]]

    sol = Solution()

    print(sol.findCircleNum(M1))

