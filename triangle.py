class Solution:
    def minimumTotal(self, triangle):
        import copy 
        path = copy.deepcopy(triangle)
        for i in xrange(len(triangle)):
            for j in xrange(len(triangle[i])):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    path[i][j] = triangle[i][j] + path[i-1][j] 
                elif j == len(triangle[i]) - 1:
                    path[i][j] = triangle[i][j] + path[i-1][j-1]
                else:
                    path[i][j] = triangle[i][j] + min(path[i-1][j], path[i-1][j-1])
        print min(path[-1])
        return min(path[-1])


test = (
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
)
x = Solution()
x.minimumTotal(test)
# Time complexity O(n^2) where n is the number of rows. This can easily be calculated using Gaussian summation
# 1 + 2 ... n in O(n^2). The only challenge of this problem is clarify on the two edge cases. 
