class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dominant =  None
        dominantCount = 0
        for n in nums:
            if dominant == None:
                print('-1-')
                dominant = n
                dominantCount += 1
            elif dominant != n:
                dominantCount -= 1
                print('-2-')
                if dominantCount == 0:
                    dominant = None
                    dominantCount = 0
            else:
                print('-3-')
                dominantCount += 1
            print(dominant, dominantCount)
        return dominant
                
