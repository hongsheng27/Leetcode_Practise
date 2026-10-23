class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        # r move right can be legal can be illegal, so sliding window doesn't work
        # prefix can calculate in N
        # (prefix - seen[prefix]) % 2 => res += 1
        # even - odd == odd
        # even - even == even
        # odd - odd == even
        # odd - even == odd

        seen = {'odd': 0, 'even': 1} # 0 as default
        prefix = res = 0
        for a in arr:
            prefix += a
            isOdd = bool(prefix % 2)
            # cal
            if isOdd:
                res += seen['even']
            else:
                res += seen['odd']
            # save
            if isOdd:
                seen['odd'] += 1 
            else:
                seen['even'] += 1

        return res % MOD