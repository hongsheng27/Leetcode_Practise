class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        # First Try: travese and find element minimal abs(i) , maintain smallest abs(i) to minValue, 
        # find num in map, find the maximual
        # OPTIMAIZE: Traverse nums, if abs(num) smaller, upadate closest, if the same, choose bigger
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                closest = max(closest, num)
        return closest


