class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furtherest = 0
        target = len(nums) - 1

        for i, num in enumerate(nums):
            if i > furtherest:
                return False
            furtherest = max(i + num, furtherest)
            if furtherest >= target:
                return True
        return True
        