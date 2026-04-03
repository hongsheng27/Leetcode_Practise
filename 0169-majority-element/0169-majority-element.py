class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lenN = len(nums)
        count = Counter(nums)
        for num, cnt in count.items():
            if cnt > lenN // 2:
                return num