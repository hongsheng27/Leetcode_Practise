# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        cur = dummy
        for _ in range(length - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next