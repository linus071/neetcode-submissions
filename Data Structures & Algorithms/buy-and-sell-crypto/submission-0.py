class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #1. Buy low and sell high
        # Brute force way running loops
        max_profit = 0

        for i in range (len(prices)):
            buy = prices[i]
            for j in range (i + 1, len(prices)):
                if(prices[j] > buy):
                    profit = prices[j] - buy 
                    max_profit = max(profit, max_profit)

        return 0 if max_profit < 0 else max_profit