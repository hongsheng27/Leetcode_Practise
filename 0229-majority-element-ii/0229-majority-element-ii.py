class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count = Counter(nums)
        res = []
        for elem, time in count.items():
            if 3 * time > n:
                res.append(elem)
        return res