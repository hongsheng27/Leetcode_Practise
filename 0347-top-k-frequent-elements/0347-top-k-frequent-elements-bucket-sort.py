class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for j in range(len(freq) - 1, 0 , -1):
            for n in freq[j]:
                res.append(n)
                if(len(res) == k): return res    
