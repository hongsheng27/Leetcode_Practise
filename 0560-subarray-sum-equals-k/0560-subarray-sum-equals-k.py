class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = 0
        res = 0
        total = 0
        
        seen = defaultdict(int)
        seen[0] = 1
        for n in nums:
            p += n
            if p - k in seen:
                res += seen[p - k]
            seen[p] += 1
        return res