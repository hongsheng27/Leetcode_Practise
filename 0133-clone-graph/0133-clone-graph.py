"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldToNew = {}
        q = deque([node])
        seen = set([node])
        while q:
            n = q.popleft()
            oldToNew[n] = Node(n.val)
            for nei in n.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        q = deque([node])
        seen = set([node])
        while q:
            n = q.popleft()
            newNei = []
            for nei in n.neighbors:
                newNei.append(oldToNew[nei])
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
            oldToNew[n].neighbors = newNei
        return oldToNew[node]

            