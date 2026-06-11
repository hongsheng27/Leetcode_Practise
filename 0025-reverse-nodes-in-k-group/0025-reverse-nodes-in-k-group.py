# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = preGroupTail = ListNode(0, head)
        while True:
            cur = preGroupTail
            # check
            for _ in range(k):
                cur = cur.next
                if not cur:
                    return dummy.next

            groupNext = cur.next
            # reverse
            prev = groupNext
            cur = preGroupTail.next
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            tmp = preGroupTail.next
            preGroupTail.next = prev
            preGroupTail = tmp