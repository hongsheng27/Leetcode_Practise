class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # solution 2: preix to save how many odds
        # seen to save {how many: amount}
        # find prefix - prePrefix == 0 in seen
        # res += amount
        prefix = 0
        seen = {0: 1}
        res = 0
        for num in nums:
            prefix += 1 if num % 2 else 0

            if prefix - k in seen:
                res += seen[prefix - k]
            
            seen[prefix] = seen.get(prefix, 0) + 1
        return res
