class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        nums_index = [(num, i) for i, num in enumerate(nums)]
        nums_index.sort(key = lambda x:x[0])
        
        res = nums_left = len(nums_index)
        last_index = 0
        for num, index in nums_index: 
            if last_index > index:
                res += nums_left
            last_index = index
            nums_left -= 1
        return res