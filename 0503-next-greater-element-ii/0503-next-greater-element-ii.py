class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [] # (position, number)
        for i in range(len(nums) * 2):
            j = i % len(nums)
            while stack and stack[-1][1] < nums[j]:
                p, n = stack.pop()
                res[p] = nums[j]
            if i < len(nums):
                stack.append((i, nums[i]))
        return res



