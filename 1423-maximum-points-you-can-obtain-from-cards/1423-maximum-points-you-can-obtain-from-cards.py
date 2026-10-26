class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # get biggest point => sum - minimal continous N - k subarray sum
        # N - k fixed window
        total = minSubArraySum = sum(cardPoints)
        windowLen = len(cardPoints) - k
        subArraySum = l = 0
        for i in range(windowLen):
            subArraySum += cardPoints[i]
        minSubArraySum = subArraySum

        for r in range(windowLen, len(cardPoints)):
            subArraySum += cardPoints[r]
            subArraySum -= cardPoints[l]
            l += 1
            minSubArraySum = min(minSubArraySum, subArraySum)
        return total - minSubArraySum