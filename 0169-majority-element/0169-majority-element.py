class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dominant =  None
        dominantCount = 0
        for n in nums:
            if dominant == None:
                dominant = n
                dominantCount += 1
            elif dominant != n:
                dominantCount -= 1
                if dominantCount == 0:
                    dominant = None
                    dominantCount = 0
            else:
                dominantCount += 1
        return dominant
                
