class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        leastWeight = r
        while l <= r:
            m = (l + r) // 2

            total = 0
            group = 1
            for w in weights:
                if total + w > m:
                    total = 0
                    group += 1
                total += w

            if group <= days:
                leastWeight = min(leastWeight, m)
                r = m - 1
            else:
                l = m + 1
        return leastWeight
                
        