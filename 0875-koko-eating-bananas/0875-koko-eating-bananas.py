class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = max(piles)
        l = 1
        r = maxValue
        res = float('inf')
        while l <= r:
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += ((p + m - 1) // m)
            if total <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

        