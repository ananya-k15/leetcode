class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = len(prices)
        buy = 0
        sell = 1
        profit = 0
        while(sell < x) : 
            diff = prices[sell] - prices[buy]
            if diff >= 0 : 
                sell += 1
                if diff > profit : 
                    profit = diff
            elif diff < 0 : 
                buy = sell
                sell += 1
            # profit += [j - prices[i] for j in prices[i+1:] if j > prices[i]]
        return profit
        