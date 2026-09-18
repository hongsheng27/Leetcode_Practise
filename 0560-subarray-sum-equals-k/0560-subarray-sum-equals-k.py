class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        prefix = res = 0
        for num in nums:
            prefix += num
            if prefix - k in seen:
                res += seen[prefix - k]
            seen[prefix] += 1
        return res