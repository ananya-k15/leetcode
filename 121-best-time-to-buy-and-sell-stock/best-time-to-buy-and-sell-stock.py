class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 # just not buy any stock

        i, j = 0, 1
        while i <= j and j < len(prices):
            day = prices[j] - prices[i]
            if day < 0:
                i += 1
            else:
                profit = max(profit, day)
                j += 1
        
        return profit