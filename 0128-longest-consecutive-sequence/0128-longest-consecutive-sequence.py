class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxTotal = 0
        for i in seen:
            if i - 1 not in seen:
                j = i
                total = 0
                while j in seen:
                    total += 1
                    j += 1
                maxTotal = max(total, maxTotal)
        return maxTotal
