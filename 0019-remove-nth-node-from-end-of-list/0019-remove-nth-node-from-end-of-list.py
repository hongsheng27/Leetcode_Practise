# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        sz = 0

        while cur:
            sz += 1
            cur = cur.next
        nth = sz - n - 1

        cur = dummy
        while nth:
            cur = cur.next
            nth -= 1

        if n != 1:
            cur.next = cur.next.next
        else:
            cur.next = None

        return dummy.next


        