class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort first, so we can avoid repeat by jumpping out the same adj elem
        # also since we sort, we can use two pointer 
        # -4 -1 -1 0 1 2 
        # 0 0 0 0 0 1 1 2
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            diff = -nums[i]
            l = i + 1
            r = len(nums) - 1
            if i - 1 >= 0 and nums[i - 1] == nums[i]: 
                continue
            while l < r:
                if nums[l] + nums[r] == diff:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while r >= 0 and r + 1 < len(nums) and nums[r] == nums[r + 1]:
                        r -= 1
                if nums[l] + nums[r] < diff:
                    l += 1
                else:
                    r -= 1
        return res


        