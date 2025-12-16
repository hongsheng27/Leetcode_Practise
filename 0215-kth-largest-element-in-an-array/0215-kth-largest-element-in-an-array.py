class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        res = 0
        for _ in range(k):
            res = -heapq.heappop(nums)
        return res
        