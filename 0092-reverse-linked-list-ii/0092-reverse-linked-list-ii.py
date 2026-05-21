# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = preLeft = ListNode(0, head)
        for _ in range(left - 1):
            preLeft = preLeft.next
        
        cur = preLeft.next 

        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        preLeft.next.next = cur
        preLeft.next = prev
        return dummy.next

    