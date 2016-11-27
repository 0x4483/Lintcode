class Solution:
    def longestIncreasingSubsequence(self, nums):
        if len(nums) < 2:
            return len(nums) 
        F = [1 for _ in xrange(len(nums))] 
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    F[i] = max(F[i], F[j] + 1) 
        return max(F) 
        
# Time: O(n^2) using DP 
# Space: O(n) 
# Comment: update only when it is increasing. F[i] stores the 
#          length of longest sequence upto index i 
# Test Case: [3, 9, 10, 0, 0, 11] 
