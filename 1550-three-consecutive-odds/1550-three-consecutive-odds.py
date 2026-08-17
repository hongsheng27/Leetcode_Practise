class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            good = 3
            for j in range(3):
                if arr[i + j] % 2: good -= 1
            if not good: return True
        return False