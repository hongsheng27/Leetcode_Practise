class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums = nums[:-1]
        if not nums: return True
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] >= n - i:
                 return self.canJump(nums)
        return False

            
        