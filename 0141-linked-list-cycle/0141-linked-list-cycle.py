# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = {}
        while head:
            count[head] = 1 + count.get(head, 0)
            if count[head] > 1:
                return True
            head = head.next
        return False