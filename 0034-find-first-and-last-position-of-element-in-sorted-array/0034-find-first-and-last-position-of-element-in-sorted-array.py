class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                if nums[m] == target:
                    left = m
                r = m - 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            else:
                if nums[m] == target:
                    right = m
                l = m + 1
        return [left, right]

