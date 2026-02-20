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
        while cur.next:
            cur = cur.next
            size += 1
        cur.next = head

        k = k % size
        
        newTail = head
        for _ in range(size - k - 1):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None
        return newHead
       


        