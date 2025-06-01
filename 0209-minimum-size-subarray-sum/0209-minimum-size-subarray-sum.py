class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        cur_sum = nums[0]
        min_len = float('inf')
        while r < len(nums):
            if cur_sum < target:
                r += 1
                if r < len(nums):
                    cur_sum += nums[r]
            else:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        return 0 if min_len == float("inf") else min_len
                

            

                