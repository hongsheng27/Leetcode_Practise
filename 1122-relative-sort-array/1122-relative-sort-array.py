class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # keep arr2 for order
        # map count of arr1: O(M)
        # traverse arr2, put each count[arr1] and freq to result, and del it: O(N)
        # sort the rest and put it res O(U log U)
        # sc: O(M + N + U log U)) / sc: O(N)
        count = Counter(arr1)
        res = []
        for num in arr2:
            res += [num] * count[num]
            del count[num]
        rest = sorted(count)
        for r in rest:
            res += [r] * count[r]
        return res
        
        
            
