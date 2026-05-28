class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums) * 2):
            i1 = i % len(nums)
            while stack and stack[-1][1] < nums[i1]:
                index, value = stack.pop()
                res[index] = nums[i1]
            if i < len(nums):
                stack.append((i, nums[i]))
        return res
        