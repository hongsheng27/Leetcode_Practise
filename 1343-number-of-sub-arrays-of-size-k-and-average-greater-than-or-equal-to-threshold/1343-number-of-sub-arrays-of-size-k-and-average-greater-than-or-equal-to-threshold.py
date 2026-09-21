class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        windowSum = res = 0
        for i in range(k):
            windowSum += arr[i]
        if windowSum / k >= threshold: res += 1

        for i in range(1, len(arr) - k + 1):
            windowSum += arr[i + k - 1]
            windowSum -= arr[i - 1]
            if windowSum / k >= threshold: res += 1
        return res
            