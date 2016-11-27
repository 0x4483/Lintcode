
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

    def canJump_greedy(self, A):
        max_index = 0 
        cur_index = 0 
        for i in xrange(len(A)):
            if cur_index < i:
                cur_index = max_index 
            # Check Impossible Jumps
            if max_index <= i and A[i] == 0 and i != len(A) - 1:
                return False
            max_index = max(max_index, A[i] + i) 
        return max_index >= len(A) - 1
    
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Best Optimized Solution. 
# Notice: we need to check situtaions where we simply cannot jump forwards.
#         It happens when we haven't reached the end (i != len(A) - 1) and 
#         we cannot jump further (A[i] == 0) and we cannot even reach index i
#         (max_index <= i)


