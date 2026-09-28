class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        res = 0
        minHeap = arr
        heapq.heapify(minHeap)
        for i in range(1, len(arr) + 1):
            elem = heapq.heappop(minHeap)
            if elem > res:
                res += 1
        return res

