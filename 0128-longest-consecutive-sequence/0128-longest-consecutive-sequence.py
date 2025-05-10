class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)

        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                longest = max(length, longest)  
        return longest


        