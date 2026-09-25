class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            # judge if success
            consecutive = res = 0
            isSuccess = False
            for b in bloomDay:
                if b <= mid:
                    consecutive += 1
                    if consecutive >= k:
                        res += 1
                        consecutive = 0
                else:
                    consecutive = 0
            if res >= m:
                isSuccess = True
            # BS
            if isSuccess:
                r = mid
            if not isSuccess:
                l = mid + 1
        return r


            

        # window size = k
        # if condition work => res += 1