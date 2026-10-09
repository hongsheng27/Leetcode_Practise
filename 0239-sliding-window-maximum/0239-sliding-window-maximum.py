class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # brute force: each window to calculate max(window), O(nk), 10^10 won't pass
        # heap solution might be work, n log n might align with 10 ^ 5
        res = []
        maxHeap = []
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
        res.append(-maxHeap[0])
        invisible = defaultdict(int)
        l = 0
        for r in range(k, len(nums)):
            heapq.heappush(maxHeap, -nums[r])
            invisible[nums[l]] += 1
            l += 1
            
            while maxHeap and -maxHeap[0] in invisible:
                elem = heapq.heappop(maxHeap)
                invisible[-elem] -= 1
                if not invisible[-elem]: del invisible[-elem]
            if maxHeap: res.append(-maxHeap[0])
        return res
            



