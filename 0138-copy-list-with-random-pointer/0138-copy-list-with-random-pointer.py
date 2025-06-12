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
        curr = head
        oldToCopy = {None: None}
    
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            oldToCopy[curr].next = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next
       
        return oldToCopy[head]
