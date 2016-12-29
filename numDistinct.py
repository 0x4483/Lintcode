class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        m = len(S) 
        n = len(T) 
        DP = [[1 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1): 
                DP[i][j] = DP[i - 1][j]
                if S[i - 1] == T[j - 1]:
                    DP[i][j] += DP[i - 1][j - 1]
        
        return DP[-1][-1]
                
