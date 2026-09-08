from collections import defaultdict

class Solution:
    def countCyclicPairs(self, nums):
      group = defaultdict(int)
      for n in nums:
        s = str(n)
        doubled = s + s
        key = s
        for j in range(len(s)):
          rotation = doubled[j: j + len(s)]
          key = min(key, rotation)
        group[key] += 1
      res = 0
      for count in group.values():
        res += count * (count - 1) // 2
      return res
        