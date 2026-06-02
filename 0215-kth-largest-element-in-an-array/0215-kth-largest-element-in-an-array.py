class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        res = 0
        for _ in range(k):
            res = -heapq.heappop(heap)
        return res