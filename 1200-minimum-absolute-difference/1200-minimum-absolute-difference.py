class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # brute force: double loop, if abs(arr[i] - arr[j]) smaller, update it , replace res with new array
        # 4: 50 but blute foce souldn't be work, because 10 ^5 cant't accept O(n^2)
        # but, maybe can accepted by (nlog n )
        # solution 2: sort first, answer only exist between n & n + 1, then we can use previous way
        # 10: 17
        arr.sort()
        minDifference = arr[1] - arr[0]
        res = [[arr[0], arr[1]]]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] < minDifference:
                minDifference = arr[i + 1] - arr[i]
                res = [[arr[i], arr[i + 1]]]
            elif arr[i + 1] - arr[i] == minDifference:
                res.append([arr[i], arr[i + 1]])
        return res