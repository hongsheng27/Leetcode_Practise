class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        count = {}
        maxTotal = total = 0
        
        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1
            total += nums[r]
            if r >= k:
                l = r - k
                total -= nums[l]
                count[nums[l]] = count.get(nums[l], 0) - 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
            if len(count) == k:
                maxTotal = max(maxTotal, total)
        return maxTotal
            

