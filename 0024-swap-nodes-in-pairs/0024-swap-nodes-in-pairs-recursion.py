# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        def recursion(node):
            if not node or not node.next: return node
            nxt = node.next
            rest = nxt.next
            nxt.next = node
            node.next = recursion(rest)
            return nxt
    
        return recursion(head)