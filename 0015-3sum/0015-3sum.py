class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort first, so we can avoid repeat by jumpping out the same adj elem
        # also since we sort, we can use two pointer 
        # -4 -1 -1 0 1 2 
        # 0 0 0 0 0 1 1 2
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:        
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res