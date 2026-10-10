class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        minValue = min(position)
        maxValue = max(position)
        position.sort()
        positionSet = set(position)
        l = 1
        r = (maxValue - minValue) // (m - 1)
    
        def isForceWork(force):
            ball = 1
            last = minValue
            for i in range(1, len(position)):
                if position[i] - last >= force:
                    last = position[i]
                    ball += 1
            return ball >= m
                
        while l < r:
            mid = (l + r + 1) // 2
            if isForceWork(mid):
                l = mid
            else:
                r = mid - 1
        return l

        