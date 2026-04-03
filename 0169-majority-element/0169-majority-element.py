class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = cnt = 0
        
        for n in nums:
            if cnt == 0:
                me = n

            if n == me:
                cnt += 1
            else:
                cnt -= 1
        return me
