# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def recursion(node):
            # basecase
            if not node: return None
            # recurrence relation
            newHead = node

            if node.next:
                newHead = recursion(node.next)
                node.next.next = node
            node.next = None

            return newHead
        return recursion(head)