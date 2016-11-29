class Solution:

    def maxProfit(self, prices):
        profit = 0
        for i in xrange(1, len(prices)):
            gain = prices[i] - prices[i-1] 
            if gain > 0:
                profit += gain
        return profit
        
# Time: O(n)
# Space: O(1) 
# Comment: DP profit keeps track the max profit we gain at time i. 
