class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = {0 : 1}
        res = prefix = 0
        for num in nums:
            prefix += num
            remainder = prefix % k
            if remainder in count:
                res += count[remainder]
            count[remainder] = count.get(remainder, 0) + 1
        return res
        
        # (prefix[i] - prefix[j]) % k = 0
        # prefix[i] % k = prefix[j] % k

        