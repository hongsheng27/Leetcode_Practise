"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}
        cur = head
        while cur:
            newNode = Node(cur.val)
            oldToNew[cur] = newNode
            cur = cur.next

        cur = head
        while cur:
            newNext = oldToNew[cur.next]
            newRandom = oldToNew[cur.random]
            oldToNew[cur].next = newNext
            oldToNew[cur].random = newRandom
            cur = cur.next
        return oldToNew[head]