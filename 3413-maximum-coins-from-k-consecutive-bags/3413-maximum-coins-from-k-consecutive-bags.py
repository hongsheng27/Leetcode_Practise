class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        res = 0
        n = len(coins)

        left = bag = 0
        for right in range(n):
            l, r, c = coins[right]
            bag += (r - l + 1) * c
            windowStart = r - k + 1

            while left <= right and coins[left][1] < windowStart:
                x, y, coin = coins[left]
                bag -= (y - x + 1) * coin
                left += 1 
            current = bag
            
            if left <= right:
                x, y, c = coins[left]
                if x < windowStart:
                    outsideLength = windowStart - x
                    current -= outsideLength * c
            res = max(res, current)

        right = n - 1
        bag = 0
        for left in range(n - 1, -1, -1):
            l, r, coin = coins[left]
            bag += (r - l + 1) * coin
            windowEnd = l + k - 1

            while left <= right and coins[right][0] > windowEnd:
                x, y, c = coins[right]
                bag -= (y - x + 1) * c
                right -= 1
            current = bag
            if left <= right:
                x, y, c = coins[right]
                if y >= windowEnd:
                    outsideLength = y - windowEnd
                    current -= outsideLength * c
            res = max(res, current)
        return res


            