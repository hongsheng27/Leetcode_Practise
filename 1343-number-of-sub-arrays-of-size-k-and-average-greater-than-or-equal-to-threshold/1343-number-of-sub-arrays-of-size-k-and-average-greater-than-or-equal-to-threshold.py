class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        
        windowSum = sum(arr[:k])
        res = 1 if windowSum >= threshold else 0

        for r in range(k, len(arr)):
            windowSum += arr[r]
            windowSum -= arr[r - k]
            if windowSum >= threshold: res += 1
        return res
            