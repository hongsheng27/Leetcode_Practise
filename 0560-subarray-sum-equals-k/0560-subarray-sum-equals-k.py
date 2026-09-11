class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1
        res = 0
        for n in nums:
            prefix += n
            if prefix - k in seen:
                res += seen[prefix - k]
            seen[prefix] += 1
        return res