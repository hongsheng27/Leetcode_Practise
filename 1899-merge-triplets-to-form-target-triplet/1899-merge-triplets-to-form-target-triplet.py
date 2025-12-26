class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                if t[0] == target[0]: found[0] = True
                if t[1] == target[1]: found[1] = True
                if t[2] == target[2]: found[2] = True
        return all(found)

        