
class Solution:
    def canJump_DP(self, A):
        DP = [False for _ in xrange(len(A))] 
        DP[0] = True
        for i in xrange(len(A)):
            for j in xrange(i):
                if DP[j] and A[j] + j >= i:
                    DP[i] = True
        return DP[-1] 
# Time Complexity: O(n^2) with two loops each in worst case runs n times. 
# Space Complexity: O(n) with a list of space n. 


