class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # find fisrt elem
        # travese + 1 if in seen set()
        seen = set(nums)
        res = 0
        for num in list(seen):
            if num - 1 not in seen:
                length = 0
                while num in seen:
                    num += 1
                    length += 1
                res = max(res, length)
        return res