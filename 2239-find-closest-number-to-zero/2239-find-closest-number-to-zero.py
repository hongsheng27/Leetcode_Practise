class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        # travese and find element minimal abs(i) , maintain smallest abs(i) to minValue, 
        # find num in map, find the maximual
        closet = nums[0]
        for num in nums:
            if abs(num) < abs(closet):
                closet = num
            elif abs(num) == abs(closet):
                closet = max(closet, num)
        return closet


