class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        l = 0
        r = k - 1   
        helper(0, n - 1)  
        helper(l, r)
        helper(r + 1, n - 1)
        


        