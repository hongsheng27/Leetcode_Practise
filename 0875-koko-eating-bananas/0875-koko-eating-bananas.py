class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r:
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / m)
            if total <= h:
                r = m
            else:
                l = m + 1
        return l
            

        