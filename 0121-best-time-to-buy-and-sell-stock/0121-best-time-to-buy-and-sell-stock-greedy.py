class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for p in prices:
            minPrice = min(minPrice, p)
            profit = max(profit, p - minPrice)
        return profit

        