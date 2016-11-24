
class Solution:
    def minPathSum(self, grid):
        m = len(grid)  
        n = len(grid[0])
        path = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    path[i][j] = grid[i][j]
                elif i == 0:
                    path[i][j] = grid[i][j] + path[i][j-1]
                elif j == 0:
                    path[i][j] = grid[i][j] + path[i-1][j]
                else:
                    path[i][j] = (min(path[i-1][j], path[i][j-1]) + 
                                      grid[i][j])
        return path[-1][-1]

x = Solution()
test = (
[[0, 1, 2], 
 [1, 0, 3], 
 [1, 2, 3]]
 )
x.minPathSum(test)

# Time Complexity: O(mn) Space Complexity: O(mn) 
# Using Dynamic Programming, we only need to consider the four 
# cases inside the inner for loop. 

# Finis 
