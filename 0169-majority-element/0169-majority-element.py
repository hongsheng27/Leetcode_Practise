class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = ""
        cnt = 0
        for n in nums:
            if not me: me = n

            if n == me:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                me = ""
        return me
