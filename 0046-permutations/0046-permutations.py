class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]

        for i in range(len(nums)):
            nextPerm = []
            for p in perm:
                for j in range(len(p) + 1):
                    copyP = p.copy()
                    copyP.insert(j, nums[i])
                    nextPerm.append(copyP)
            perm = nextPerm
        return perm


        