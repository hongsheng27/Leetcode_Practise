class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # sliding window doesn't work, since r don't know how to stop
        # prefix, save remainer in seen
        # at least two
        seen = set()
        res = prefix = 0
        for num in nums:
            prefix += num
            remainder = prefix % k

            if remainder in seen:
                return True
            
            seen.add((prefix - num) % k)
        return False