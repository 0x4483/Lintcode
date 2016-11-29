import sys
class Solution:
    def maxProfit_bruteForce(self, prices):
        max_profit = 0
        for i in xrange(len(prices)): 
            if i > 0:
                profit = prices[i] - min(prices[:i])
                if profit > max_profit:
                    max_profit = profit 
        return max_profit
# Time: O(n^2)
# Spce: O(1) 
# Comments: Brute Force
        
    def maxProfit(self,prices):
        max_profit = 0
        min_price =sys.maxint
        for price in prices:
            if price < min_price:
                min_price = price
            if max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit 
        
# Time: O(n) 
# Space: O(1) 
# Comments: DP track max_profit and min_price 
