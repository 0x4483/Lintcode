class Solution: 
    def minDistance(self, word1, word2):
        lw2 = len(word2) + 1
        lw1 = len(word1) + 1
        F = [[j for j in xrange(lw2)] for _ in xrange(lw1)] 
        for i in xrange(lw1):
            F[i][0] = i 
        for i in xrange(1, lw1):
            for j in xrange(1, lw2):
                if word1[i-1] == word2[j-1]:
                    F[i][j] = F[i-1][j-1]
                else:
                    F[i][j] = min(F[i-1][j], F[i][j-1], F[i-1][j-1]) + 1
        return F[-1][-1]
        
# Time: O(mn) m is length of word1 and n is length of word2 
# Space: O(mn) 
# F[i][j] is the minDistance to transform word1[:i] to word2[:j]
# Two cases to consider. First case is when last elements are same, then F[i-1][j-1] is the desired answer
# Second case is when they are not the same, then three subcases: insert, delete or replace operatins. 
