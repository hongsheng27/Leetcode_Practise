class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        res = []
        isUploadNewInteval = False
        for i, interval in enumerate(intervals):
            # before newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)
            # after newInterval
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                res += intervals[i:]
                isUploadNewInteval = True
                break
            # overlap
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if not isUploadNewInteval: res.append(newInterval)
        return res
        