class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        # left shrinking cannot make window become leagal stabley, so sliding window doesn't work
        # prefix can calculate in N
        # currentPrefix - previousPrefix % 2 = 1
        # even - odd == odd
        # odd - even == odd
        # even - even == even
        # odd - odd == even

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