class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # subarray, find multiple of k, since we have negative number, can't use sliding window
        # using prfix, prefix[i] - prefix[j] should be multiple of k
        # 05: 00
        prefix = res = 0
        seen = {0: 1} # prefix: amount
        for num in nums:
            prefix += num
            
            if (prefix - k) % k in seen:
                res += seen[(prefix - k) % k]
            
            seen[prefix % k] = seen.get(prefix % k, 0) + 1
        return res
        # 15:00 done debug