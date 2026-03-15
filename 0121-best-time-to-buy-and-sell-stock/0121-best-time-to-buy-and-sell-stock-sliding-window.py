class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, profit = 0, 0

        for r in range(len(prices)):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return profit
            
        