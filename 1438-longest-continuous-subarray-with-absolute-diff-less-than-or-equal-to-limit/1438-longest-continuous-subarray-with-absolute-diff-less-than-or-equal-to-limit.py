class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxQ = deque()
        minQ = deque()
        l = res = 0
        for r in range(len(nums)):
            while maxQ and nums[maxQ[-1]] < nums[r]:
                maxQ.pop()
            while minQ and nums[minQ[-1]] > nums[r]:
                minQ.pop()
            maxQ.append(r) 
            minQ.append(r)
            print('1', nums[maxQ[0]], nums[minQ[0]])
            while maxQ and minQ and abs(nums[maxQ[0]] - nums[minQ[0]]) > limit:
                l += 1
                if maxQ[0] < l: maxQ.popleft()
                if minQ[0] < l: minQ.popleft()
            res = max(res, r - l + 1)
        return res
                
            
        