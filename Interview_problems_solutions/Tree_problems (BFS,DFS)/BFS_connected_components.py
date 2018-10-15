class Solution(object):
    '''
    Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.
    '''    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        visited = set()
        valid_nums = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='O' and (i,j) not in visited:
                    current = (i,j)
                    numbers = self.bfs(current,board,len(board)-1,len(board[0])-1)
                    visited = visited.union(numbers)
                    if self.is_valid(list(numbers),len(board)-1,len(board[0])-1):
                        valid_nums.extend(list(numbers))

        for (i,j) in valid_nums:
            board[i][j] = 'X'
        return board
    def bfs(self,root,board,x_length,y_length):
        next_visit = [root]
        visited = set()
        while len(next_visit)>0:
            current = next_visit.pop(0)
            i = current[0]
            j = current[1]
            if i>=0 and i<=x_length and j>=0 and j<=y_length:
                if board[i][j]=='O' and (i,j) not in visited:
                    visited.add((i,j))
                    next_visit.append((i-1,j))
                    next_visit.append((i,j-1))
                    next_visit.append((i+1,j))
                    next_visit.append((i,j+1))
        return visited
            
    def is_valid(self,nums,x_max,y_max):
        for i in range(len(nums)):
            if nums[i][0]== 0 or nums[i][0]==x_max:
                return False
            if nums[i][1]==0 or nums[i][1] == y_max:
                return False
        return True


board = [['X', 'X' ,'X', 'X'],
['X', 'O', 'O', 'X']
,['X', 'X', 'O', 'X'],
['X', 'O', 'X', 'X']]

sol = Solution()
print(sol.solve(board))