class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)
        res = max_k
        while min_k <= max_k:
            middle = (min_k + max_k) // 2
            if self.is_finieshed(piles, middle, h):
                res = min(res, middle)
                max_k = middle - 1
                print('finished',min_k, max_k)
            else:
                min_k = middle + 1
                print('not finished',min_k, max_k)
        print(res)
        return res

    def is_finieshed(self, piles: List[int], k: int, h:int) -> int:
        total_hour = 0
        for i in range(len(piles)):
            total_hour += math.ceil(piles[i] / k)
        return total_hour <= h
