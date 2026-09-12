class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = Counter(nums)
        starts = set()
        for n in nums:
            if n - 1 not in count:
                starts.add(n)
        res = 0
        for start in starts:
            length = 0
            while start in count:
                length += 1
                start += 1
            res = max(res, length)
        return res