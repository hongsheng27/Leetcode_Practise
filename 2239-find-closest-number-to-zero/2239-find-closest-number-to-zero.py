class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        # brute force: travese and find element that abs(i) minimal, push nums[i]to res, 
        # find num in map
        minValue = float('inf')
        map = defaultdict(list)
        for num in nums:
            minValue = min(minValue, abs(num))
            map[abs(num)].append(num)
        return max(map[minValue])


