import sys 

class Solution:
    def jump_dp(self, A):
        F = [0 for _ in xrange(len(A))] 
        # F[i] is the minimum step to reach index i
        for i in xrange(len(A)):
            minimum = sys.maxint 
            for j in xrange(i):
                if A[j] + j >= i:
                    F[i] = min(F[j] + 1, minimum) 
                    minimum = F[i]
        return F[-1]
# Time Complexity: O(n^2) using DP to memorize the minimum steps 

    def jump_greedy(self, A):
            reached = 0
            current = 0  
            jump = 0
            for i, item in enumerate(A):
                if i > current: 
                    if item == 0:
                        return False
                    current = reached
                    jump += 1
                reached = max(reached, item + i)  
            return jump
            
# Time Complexity: O(n) using greedy algorithm 
# Test Cases:
# [1] 
# [1, 0]
# [1, 0, 0, 0, 3]
# [1, 5, 2] 
# [1, 1, 1] 
