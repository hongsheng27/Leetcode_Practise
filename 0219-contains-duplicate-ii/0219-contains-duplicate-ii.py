class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {} # (indexs)
        for i, n in enumerate(nums):
            if n not in count:
                count[n] = i
            else:
                if i - count[n] <= k:
                    return True
                count[n] = i
        return False
                    
