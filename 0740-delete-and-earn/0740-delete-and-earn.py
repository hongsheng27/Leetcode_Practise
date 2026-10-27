class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # count: {2: 4, 3: 9, 4: 4}
        # list [0, 0, 4, 9, 4]
        # dp[i] = maximal point from 0 to i
        # dp[i] = max(dp[i - 2] + list[i], dp[i - 1])
        # return dp[-1]
        # 11:10
        if len(nums) == 1: return nums[0]
        count = Counter(nums)
        maxVal = max(nums)
        dp = [0] * (maxVal)
        lst = [0] * (maxVal)
        
        for num, freq in count.items():
            lst[num - 1] = num * freq

        print(dp, lst)
        if len(lst) == 1: return lst[0]
        
        dp[0] = lst[0]
        dp[1] = max(lst[0], lst[1])
        for i in range(2, maxVal):
            dp[i] = max(dp[i - 2] + lst[i], dp[i - 1])
        return dp[-1]
        # 19:00

        