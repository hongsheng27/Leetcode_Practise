class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = leastWeight = sum(weights)
        while l <= r:
            m = (l + r) // 2
            total = d = 0
            for i in range(len(weights)):
                total += weights[i]
                if i == len(weights) - 1 or i < len(weights) and total + weights[i + 1] > m:
                    d += 1
                    total = 0
            if d <= days:
                leastWeight = min(leastWeight, m)
                r = m - 1
            else:
                l = m + 1
        return leastWeight

        