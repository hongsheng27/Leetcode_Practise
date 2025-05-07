class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for e in nums:
            if e in count:
                count[e] += 1
            else:
                count[e] = 1
        array = list(count.items())
        array.sort(key= lambda x: x[1]) # [("3",1),("2",2),("1",3)]
        print(array, [x[0] for x in array[-k:] ])
        return [x[0] for x in array[-k:]]
        