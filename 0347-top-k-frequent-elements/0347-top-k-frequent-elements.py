class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        
        for i in count.keys():
            freq[count[i]].append(i)
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                k -= 1
                if k == 0: return res