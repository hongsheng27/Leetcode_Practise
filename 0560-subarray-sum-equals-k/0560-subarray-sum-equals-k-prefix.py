class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = 0
        freq = {0: 1}
        for num in nums:
            prefixSum += num

            if prefixSum - k in freq:
                res += freq[prefixSum - k]
            
            freq[prefixSum] = freq.get(prefixSum, 0) + 1
        return res
