class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        minWeight = r = sum(weights)
        while l <= r:
            m = (l + r) // 2
            total = 0
            d = 0
            for i, w in enumerate(weights):
                total += w
                if i + 1 < len(weights) and total + weights[i + 1] > m:
                    d += 1
                    total = 0
            d = d + 1 if total > 0 else d
            if d <= days:
                minWeight = min(minWeight, m)
                r = m - 1
            else:
                l = m + 1
        return minWeight
            