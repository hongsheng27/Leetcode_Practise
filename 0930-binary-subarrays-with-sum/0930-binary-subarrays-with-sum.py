class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # pattern observation: subarray, cumulative value => prefix
        seen = {0: 1} # blance: amount
        balance = 0
        res = 0
        for num in nums:
            balance += 1 if num == 1 else 0
            if balance - goal in seen:
                res += seen[balance - goal]
            seen[balance] = seen.get(balance, 0) + 1
        return res