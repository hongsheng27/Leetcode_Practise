class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        if nums.count(candidate1) > len(nums) // 3:
            res.append(candidate1)
        if nums.count(candidate2) > len(nums) // 3:
            res.append(candidate2)
        return res
        


