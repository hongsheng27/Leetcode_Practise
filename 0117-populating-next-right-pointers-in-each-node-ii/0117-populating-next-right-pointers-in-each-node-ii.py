"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        
        while head:
            dummy = tail = Node()
            cur = head
            while cur:
                if cur.left:
                    tail.next = cur.left 
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right 
                    tail = tail.next
                cur = cur.next
            head = dummy.next
        return root
     