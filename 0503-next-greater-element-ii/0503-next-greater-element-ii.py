class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = [] # (index, number)
        res = [-1] * n
        for i in range(n * 2):
            i1 = i % n
            while stack and stack[-1][1] < nums[i1]:
                index, number = stack.pop()
                res[index] = nums[i1]
            if i < n:
                stack.append((i, nums[i]))
        return res
        