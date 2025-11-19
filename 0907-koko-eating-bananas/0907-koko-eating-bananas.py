class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)

        while min_k <= max_k:
            m = (min_k + max_k) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / m)

            if hour <= h:
                max_k = m - 1
            else:
                min_k = m + 1
        return min_k

            