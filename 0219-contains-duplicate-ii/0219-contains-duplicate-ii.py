class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {} # (cnt, (indexs))
        for i, n in enumerate(nums):
            if n not in count:
                count[n] = [1, [i]]
            else:
                count[n][0] += 1
                count[n][1].append(i)
                if count[n][0] >= 2 and count[n][1][-1] - count[n][1][-2] <= k:
                    return True
        return False
                    
