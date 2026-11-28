class Solution:
    def trap(self, height: list[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        rightMost = 0
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = rightMost
            rightMost = max(rightMost, height[i])
        leftMost = 0
        for i in range(len(height) - 1):
            prefix[i] = leftMost
            leftMost = max(leftMost, height[i])
        res = 0
        for i in range(len(height) - 1):
            print(res)
            res += max(min(prefix[i], suffix[i]) - height[i], 0)
        return res

