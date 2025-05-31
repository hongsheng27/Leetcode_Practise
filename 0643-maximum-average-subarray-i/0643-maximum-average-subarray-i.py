class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = 0
        for i in range(k):
            k_sum += nums[i]
        maximum_average = k_sum / k

        for j in range(k, len(nums)):
            k_sum = k_sum + nums[j] - nums[j-k]
            maximum_average = max(maximum_average, k_sum / k)
        return maximum_average

            

            