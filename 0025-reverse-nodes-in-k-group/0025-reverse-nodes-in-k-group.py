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
            for _ in range(k):
                cur = cur.next
                if not cur:
                    return dummy.next
            nextGroupHead = cur.next
            cur.next = None
            # reverse
            prev = None
            cur = preGroupTail.next
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            firstElem = preGroupTail.next
            firstElem.next = nextGroupHead
            preGroupTail.next = prev
            preGroupTail = firstElem

            