class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastIndex = {} 
        for i, n in enumerate(nums):
            if n in lastIndex and i - lastIndex[n] <= k:
                return True
            lastIndex[n] = i
        return False
                    
