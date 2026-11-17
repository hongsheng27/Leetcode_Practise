# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        def recursion(node):
            if not node: return None
            nxt = node.next
            if nxt:
                nextHead = nxt.next
                nxt.next = node
                node.next = recursion(nextHead)
                return nxt
            else:
                return node
        return recursion(head)