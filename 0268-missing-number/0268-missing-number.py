class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = set()
        for i in range(len(nums) + 1):
            target.add(i)
        for n in nums:
            if n in target:
                target.remove(n)
        return target.pop()

        