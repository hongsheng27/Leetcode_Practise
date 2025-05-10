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
                span = 1
                while num + span in nums_set:
                    span += 1
                longest = span if span > longest else longest    
        return longest

        return len(res) + 1

        