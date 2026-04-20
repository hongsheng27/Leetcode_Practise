class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1
        N = len(nums)
        k = k % N

        # Reverse all
        reverse(0, N - 1)
        # Reverse first k
        reverse(0, k - 1)
        # Reverse rest
        reverse(k, N - 1)

        
