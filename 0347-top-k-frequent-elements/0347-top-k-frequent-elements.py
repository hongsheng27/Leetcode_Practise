class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)] # include 0 bucket
        res = []
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                k -= 1
                if k == 0: return res