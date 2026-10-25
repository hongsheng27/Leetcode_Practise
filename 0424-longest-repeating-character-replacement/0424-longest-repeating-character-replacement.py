class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window: move right, while become illegal, move left to become legal
        # record ans while legal
        # condition: leading A, other like B can only have k, or illegal
        # leading letter => O(26)
        # 9: 30
        l = res = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            leadingAmount = max(count.values())
            while k < (r - l + 1) - leadingAmount:
                count[s[l]] -= 1
                if not count[s[l]]: del count[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
        # 18: 40 debug

        