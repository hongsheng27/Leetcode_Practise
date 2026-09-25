class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        count = {}
        maxTotal = total = 0
        for r in range(k):
            count[nums[r]] = count.get(nums[r], 0) + 1
            total += nums[r]

        if len(count) == k:
            maxTotal = max(maxTotal, total)
        
        for r in range(k, len(nums)):
            l = r - k
            total += nums[r]
            total -= nums[l]
            count[nums[r]] = count.get(nums[r], 0) + 1
            count[nums[l]] = count.get(nums[l], 0) - 1
            if count[nums[l]] == 0:
                del count[nums[l]]
            if len(count) == k:
                maxTotal = max(maxTotal, total)
        return maxTotal
            

