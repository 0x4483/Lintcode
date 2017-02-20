# Author: Zihan
# link 1: https://youtu.be/cSQsT_blRhM
# link 2: https://youtu.be/bwkDgVgT1yk

# Solution 1 passes 88% of the test, fail on large size string s 
class Solution:
    def wordBreak(self, s, dict):
        dp = [False for _ in xrange(len(s) + 1)] 
        dp[0] = True 
        for i in xrange(len(s) + 1):
            for j in xrange(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[-1]
        
# Time Complexity: O(n^2) where n is the length of s
# space complexity: O(n) 
        
# Solution 2 passed 100% tests handling the previous failure by 
#   take account of maximum sub length we need to check 
class Solution:
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0
        dp = [False for _ in xrange(len(s) + 1)] 
        dp[0] = True 
        lengthList = [len(e) for e in dict]
        maxLength = max(lengthList) 
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, min(i, maxLength) + 1):
                if dp[i - j] and s[i - j:i] in dict:
                    dp[i] = True
                    break
        return dp[-1]
        
# Time: O(nm) where n is the length of s and m is the maximum length of element in dict
# space: O(n) 
