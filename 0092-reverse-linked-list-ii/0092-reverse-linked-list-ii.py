# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return None
        dummy = preHead = ListNode(0, head)
        # find preHead
        for _ in range(left - 1):
            preHead = preHead.next
        cur = preHead.next
        # reverse
        prev = None
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        preHead.next.next = cur
        preHead.next = prev
        return dummy.next



