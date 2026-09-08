class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        res = 0
        total = 0
        for i, n in enumerate(nums):
            total += n
            prefix[i] = total
        seen = defaultdict(int)
        seen[0] = 1
        for p in prefix:
            if p - k in seen:
                res += seen[p - k]
                print(res)
            seen[p] += 1
        return res