class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [None] * (len(nums) + 1) # include 0
        count = Counter(nums)
        for num, f in count.items():
            if freq[f]:
                freq[f].append(num)
            else:
                freq[f] = [num]
        for i in range(len(freq) - 1, 0, -1):
            if not freq[i]: continue
            for j in freq[i]:
                k -= 1
                res.append(j)
                if not k:
                    return res


        # count = Counter(nums)
        # maxHeap = [(-freq, num) for num, freq in count.items()]
        # heapq.heapify(maxHeap)
        # res = []
        # for _ in range(k):
        #     _, num = heapq.heappop(maxHeap)
        #     res.append(num)
        # return res