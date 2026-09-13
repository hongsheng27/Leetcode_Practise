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
        def dfs(n):
            if n in oldToNew: return oldToNew[n]
            oldToNew[n] = Node(n.val)
            for nei in n.neighbors:
                if nei not in oldToNew:
                    dfs(nei)
                oldToNew[n].neighbors.append(oldToNew[nei])
        dfs(node)
        return oldToNew[node]