class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}
        for i, n in enumerate(nums):
            if n in count:
                if i - count[n] <= k:
                    return True
            count[n] = i
        return False