class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furtherest = 0
        for i, num in enumerate(nums):
            furtherest = max(i + num, furtherest)
            if i == furtherest and i != len(nums) - 1:
                return False
        return True
        