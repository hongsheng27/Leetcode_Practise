class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pathway = [] # (position, pplStatus)
        for trip in trips:
            numPassenger, frm, to = trip
            pathway.append((frm, numPassenger))
            pathway.append((to, -numPassenger))
        pathway.sort()
        total = 0
        for p in pathway:
            total += p[1]
            if total > capacity: return False
        return True
