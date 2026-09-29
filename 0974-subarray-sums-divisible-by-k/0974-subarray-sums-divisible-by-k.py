class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = {0 : 1}
        res = prefix = 0
        for num in nums:
            prefix += num
            if prefix % k in count:
                res += count[prefix % k]
            count[prefix % k] = count.get(prefix % k, 0) + 1
        return res
        
        # (prefix[i] - prefix[j]) % k = 0
        # prefix[i] % k = prefix[j] % k

        