class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        res = 0
        for f in range(1, len(prices)):
            if prices[f] > prices[f - 1]: 
                res += max(prices[f] - prices[s], 0)
                s = f
            else:
                s += 1
        return res

        