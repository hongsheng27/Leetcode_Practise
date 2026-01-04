class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, subSets, curSet):
            # base case
            if i >= len(nums):
                subSets.append(curSet.copy())
                return 

            # include nums[i]
            curSet.append(nums[i])
            helper(i + 1, nums, subSets, curSet)
            curSet.pop()

            # Not include nums[i]
            helper(i + 1, nums, subSets, curSet)

        i = 0
        subSets, curSet = [], []
        helper(0, nums, subSets, curSet)
        return subSets

        