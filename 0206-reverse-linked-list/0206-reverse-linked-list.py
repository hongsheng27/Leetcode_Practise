# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def recursion(node):
            # basecase
            if not node: 
                dummy = tail = ListNode()
                return [tail, dummy]
            # recurrence relation
            t, d = recursion(node.next)
            t.next = node
            node.next = None

            return [node, d]
        return recursion(head)[1].next