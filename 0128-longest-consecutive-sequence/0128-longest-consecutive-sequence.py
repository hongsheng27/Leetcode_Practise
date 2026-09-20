class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find first
        # for set: reduce repeat
        # if in set: res += 1
        seen = set(nums)
        starts = []
        for n in seen:
            if n - 1 not in seen:
                starts.append(n)
        res = 0
        for s in starts:
            length = 0
            while s in seen:
                s += 1
                length += 1
            res = max(res, length)
        return res
