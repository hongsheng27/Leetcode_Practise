class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        window = arr 
        l = 0
        r = len(arr) - 1
        while r - l + 1 > k:
            leftDiff = abs(x - arr[l])
            rightDiff = abs(x - arr[r])
            if leftDiff <= rightDiff:
                r -= 1
            else:
                l += 1
          
        return arr[l:r+1]


        