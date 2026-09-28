class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        res = 0
        q = deque([0])
        visited = {0}
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                j = nums[i]
                for index in range(i + 1, i + j + 1):
                    if index < len(nums) and index not in visited:
                        q.append(index)
                        visited.add(index)
                        if index == len(nums) - 1: return res + 1
            res += 1
        return res