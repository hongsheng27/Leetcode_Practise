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
        cur = head
        oldToNew = {None: None}
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            new = oldToNew[cur]
            newNext = oldToNew[cur.next]
            randomNext = oldToNew[cur.random]
            new.next = newNext
            new.random = randomNext
            cur = cur.next
        return oldToNew[head]
        
        