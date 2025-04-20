class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, ele in enumerate(nums):
            remaining = target - ele
            if remaining in seen:
                return [seen[remaining],i]
            seen[ele] = i


            