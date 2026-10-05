class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # brute force: double loop, if abs(arr[i] - arr[j]) smaller, update it , replace res with new array
        # 4: 50 but blute foce souldn't be work, because 10 ^5 cant't accept O(n^2)
        # but, maybe can accepted by (nlog n )
        # solution 2: sort first, answer only exist between n & n + 1, then we can use previous way
        # 10: 17
        arr.sort()
        minDifference = float('inf')
        res = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < minDifference:
                minDifference = arr[i + 1] - arr[i]
                res = [[arr[i], arr[i + 1]]]
            elif arr[i + 1] - arr[i] == minDifference:
                res.append([arr[i], arr[i + 1]])
        return res
        # 21:22