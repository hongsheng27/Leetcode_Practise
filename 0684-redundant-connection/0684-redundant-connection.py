class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # solution1: return the edge breaking tree, mean fund edge can't be union
        # using union find
        # 4:45
        n = len(edges)
        parents = [i for i in range(n + 1)]
        sizes = [1] * (n + 1)
        def find(a):
            cur = a
            while cur != parents[cur]:
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]
            return cur

        def union(a, b):
            headA = find(a)
            headB = find(b)
            if headA == headB: return False

            if sizes[headA] < sizes[headB]:
                headA, headB = headB, headA
            parents[headB] = headA
            sizes[headA] += sizes[headB]
            return True
        
        for start, end in edges:
            if not union(start, end):
                return [start, end]
        # 18:27 done, optimzie find
        #