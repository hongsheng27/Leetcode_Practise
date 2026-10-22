class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            if prefix - k in seen:
                res += seen[prefix - k]
            if prefix not in seen:
                seen[prefix] = 0
            seen[prefix] += 1
        return res
        