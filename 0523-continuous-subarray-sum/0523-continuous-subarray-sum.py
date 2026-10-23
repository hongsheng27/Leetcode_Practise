class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # sliding window doesn't work, since r don't know how to stop
        # prefix, save remainer in seen
        # at least two
        seen = {}
        res = prefix = 0
        for num in nums:
            prefix += num
            remainder = prefix % k

            if remainder in seen:
                res += seen[remainder]
            
            seen[(prefix - num) % k] = seen.get((prefix - num) % k, 0) + 1
        return res != 0