class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # sliding window work: since move right can multiply to bigger, move left can decrease
        # move right to become illegal, move left to become legal
        l = res = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            res += (r - l + 1)
            print(res)
        return res
        # 17: 00 debug

        