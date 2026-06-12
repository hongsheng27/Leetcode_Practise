# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = cur = ListNode(0, head)
        k = right - left + 1
        for _ in range(left - 1):
            cur = cur.next
        prevHead = cur
        cur = cur.next
        prev = None
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        tmp = prevHead.next
        prevHead.next = prev
        tmp.next = cur
        return dummy.next


        