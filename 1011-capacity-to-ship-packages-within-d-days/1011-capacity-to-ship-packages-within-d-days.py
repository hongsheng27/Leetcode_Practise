class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxSum = sum(weights)
        maxValue = max(weights)
        l = 1
        r = maxSum
        res = r
        while l <= r:
            m = (l + r) // 2
            total = 0
            d = 0
            if m < maxValue: 
                l = m + 1
                continue
            for w in weights:
                if total + w > m:
                    d += 1
                    total = 0
                total += w
            d = d + 1 if total != 0 else d
            if d <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

