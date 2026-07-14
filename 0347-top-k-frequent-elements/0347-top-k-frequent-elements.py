class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(maxHeap)
        res = []
        for _ in range(k):
            _, num = heapq.heappop(maxHeap)
            res.append(num)
        return res