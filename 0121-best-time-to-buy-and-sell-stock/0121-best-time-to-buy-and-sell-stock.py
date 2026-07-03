class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        res = 0
        for price in prices:
            smallest = min(smallest, price)
            res = max(res, price - smallest)
        return res
        