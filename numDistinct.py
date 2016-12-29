class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # n is length of S
        # m is length of T
        n = len(S)
        m = len(T) 
        DP = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)] 
        DP[0] = [1 for _ in xrange(n + 1)]
        for j in xrange(1, n + 1):
            for i in xrange(1, m + 1):
                if S[j - 1] == T[i - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + DP[i][j - 1]
                else:
                    DP[i][j] = DP[i][j - 1]
        return DP[-1][-1]
