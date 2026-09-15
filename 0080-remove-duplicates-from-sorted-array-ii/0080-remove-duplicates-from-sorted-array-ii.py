class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = s = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                length = r - l
                if length >= 2:
                    s += 2
                else:
                    s += length
                l = r
                for x in range(s, r):
                    nums[x] = nums[r]
        s += (2 if r + 1 - l > 2 else r + 1 - l)
        return s