# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        cur = head
        size = 1
        while cur and cur.next:
            cur = cur.next
            size += 1
        # form a circle
        cur.next = head

        k = k % size
        # newTail => seve
        newTail = head
        for _ in range(size - k - 1):
            newTail = newTail.next
        # new Head
        newHead = newTail.next
        newTail.next = None
        return newHead
       


        