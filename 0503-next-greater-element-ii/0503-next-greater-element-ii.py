class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = [] # (index, number)
        res = [-1] * n
        for i in range(2 * n):
            while stack and stack[-1][1] < nums[i % n]:
                index, number = stack.pop()
                if index < len(nums):
                    res[index] = nums[i % n]
            stack.append((i, nums[i % n]))
        return res
        


        