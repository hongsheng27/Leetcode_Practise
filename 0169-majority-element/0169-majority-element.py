class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate =  None
        count = 0
        for n in nums:
            if candidate == None:
                candidate = n
                count += 1
            elif candidate != n:
                count -= 1
                if count == 0:
                    candidate = None
                    count = 0
            else:
                count += 1
        return candidate
                
