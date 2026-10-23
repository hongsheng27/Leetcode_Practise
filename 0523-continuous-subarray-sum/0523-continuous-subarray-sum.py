class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        seen = {0: -1} # prefix: position
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            remainder = prefix % k

            if remainder in seen and i - seen[remainder] > 1:
                return True
            elif remainder not in seen:
                seen[remainder] = i
        return False
