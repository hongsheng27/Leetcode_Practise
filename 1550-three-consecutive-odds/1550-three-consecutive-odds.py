class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            oddCount = 0
            for j in range(3):
                if arr[i + j] % 2: oddCount += 1
            if oddCount == 3: return True
        return False