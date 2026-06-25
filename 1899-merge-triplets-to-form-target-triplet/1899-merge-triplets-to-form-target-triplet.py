class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        newTriplets = []
        for triplet in triplets:
            if (triplet[0] <= target[0] and
                triplet[1] <= target[1] and
                triplet[2] <= target[2]):
                newTriplets.append(triplet)
        print(newTriplets)
        isPass = [False] * 3
        for triplet in newTriplets:
            for i in range(3):
                if triplet[i] == target[i]: 
                    isPass[i] = True
        return isPass == [True] * 3
        