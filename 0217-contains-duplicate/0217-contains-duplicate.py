class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = set()
        for i in nums:
            if i  in count:
                return True  
            count.add(i)
        return False
        