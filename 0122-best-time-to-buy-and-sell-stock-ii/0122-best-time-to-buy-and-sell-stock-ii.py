class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = len(prices)
        buy = 0
        sell = 1
        totalprofit = 0
        while(sell < x) : 
            diff = prices[sell] - prices[buy]
            if diff >= 0 : 
                while (sell < x) : 
                    if prices[sell] > prices[sell - 1] : sell += 1
                    else : break
                sell -= 1
                totalprofit += (prices[sell] - prices[buy])
                buy = sell + 1
                sell = buy + 1
            elif diff < 0 : 
                buy += 1
                sell = buy + 1 
        return totalprofit
        