class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        maxMoney = 0
        left = bag = 0
        for right in range(len(coins)):
            l, r, coin = coins[right]
            windowStart = r - k + 1
            bag += (r - l + 1) * coin

            while left < right and coins[left][1] < windowStart:
                x, y, c = coins[left]
                bag -= (y - x + 1) * c
                left += 1
            current = bag
            if left <= right:
                x, y, c = coins[left]
                if x < windowStart:
                    outsideLength = windowStart - x
                    current -= outsideLength * c
            maxMoney = max(maxMoney, current)
        
        right = len(coins) - 1
        bag = 0
        for left in range(len(coins) - 1, -1, -1):
            l, r, coin = coins[left]
            bag += (r - l + 1) * coin
            windowEnd = l + k - 1

            while left < right and coins[right][0] > windowEnd:
                x, y, c = coins[right]
                bag -= (y - x + 1) * c
                right -= 1
            current = bag
            if left <= right:
                x, y, c = coins[right]
                if y > windowEnd:
                    outsideLength = y - windowEnd
                    current -= outsideLength * c
            maxMoney = max(maxMoney, current)
        return maxMoney
            
