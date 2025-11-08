class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        max_sum = cur_sum
 
        for j in range(k, len(nums)):
            cur_sum = cur_sum + nums[j] - nums[j-k]
            max_sum = max(max_sum, cur_sum)
        return max_sum / k
            

            