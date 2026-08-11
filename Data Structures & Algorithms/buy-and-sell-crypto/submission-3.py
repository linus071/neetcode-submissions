class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two Pointer Solution
        l, r = 0,1 #left buy, right sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # l becomes r since found another price lower then current l, jump straight to r
            r += 1

        return maxP