class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        # travese and find element minimal abs(i) , maintain smallest abs(i) to minValue, 
        # find num in map, find the maximual
        minValue = float('inf')
        res = float('-inf')
        for num in nums:
            if abs(num) < minValue:
                minValue = abs(num)
                res = num
            elif abs(num) == minValue:
                res = max(res, num)
        return res


