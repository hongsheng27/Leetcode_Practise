class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        seen = defaultdict(int)
        seen[0] += 1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix[i] = total
        res = 0
        for i in range(len(nums)):
            if prefix[i] - k in seen:
                res += seen[prefix[i] - k]
            seen[prefix[i]] += 1
        return res