class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # solution 1: sliding window, since we can move left pointer leagally
       
        def atMost(_k):
            oddAmount = l = res = 0
            for r in range(len(nums)):
                if nums[r] % 2:
                    oddAmount += 1
                while oddAmount > _k:
                    if nums[l] % 2: oddAmount -= 1
                    l += 1
                if oddAmount <= _k: res += (r - l + 1)
            return res
        return atMost(k) - atMost(k - 1)


        # 06:30 debug