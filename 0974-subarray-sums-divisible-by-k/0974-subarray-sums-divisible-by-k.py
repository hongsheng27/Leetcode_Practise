class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # subarray, find multiple of k, since we have negative number, can't use sliding window
        # using prfix, prefix[i] - prefix[j] should be multiple of k
        count = {0 : 1}
        res = prefix = 0
        for num in nums:
            prefix += num
            remainder = prefix % k
            if remainder in count:
                res += count[remainder]
            count[remainder] = count.get(remainder, 0) + 1
        return res
        