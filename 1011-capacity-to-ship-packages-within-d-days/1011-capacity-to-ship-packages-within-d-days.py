class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = leastWeight = sum(weights)
        while l <= r:
            m = (l + r) // 2
            total = 0
            d = 1
            for w in weights:
                if total + w > m:
                    d += 1
                    total = 0
                total += w
            if d <= days:
                leastWeight = min(leastWeight, m)
                r = m - 1
            else:
                l = m + 1
        return leastWeight

        